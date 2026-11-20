"""Verify beta identity, owner certificate, signed feed and prepared artifacts."""
from pathlib import Path
import os,shutil,subprocess,hashlib,json,base64,tempfile,zipfile,re
ROOT=Path(__file__).resolve().parents[2]
APP='com.iluhin.fiveletters.beta'
ORIGIN='https://raw.githubusercontent.com/iluhin/app.slovoplet.beta/main/ota/'
CERT='2da8c0b059d20af21ba8c2ee6c0fa7e624802deb47bc5e55bc7253cc6be366c7'
def sdk_tool(name):
    configured=os.environ.get('BETA_'+name.upper())
    if configured:return configured
    found=shutil.which(name)
    if found:return found
    sdk=os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
    if sdk:
        paths=sorted((Path(sdk)/'build-tools').glob('*/'+name))
        if paths:return str(paths[-1])
    raise RuntimeError('Android SDK tool required: '+name)
def run(args):return subprocess.check_output(args,text=True,stderr=subprocess.STDOUT)
def payload(path):
    e=json.loads(path.read_text())
    raw=base64.b64decode(e['payload'],validate=True)
    signature=base64.b64decode(e['signature'],validate=True)
    with tempfile.TemporaryDirectory() as tmp:
        a=Path(tmp)/'payload';b=Path(tmp)/'signature'
        a.write_bytes(raw);b.write_bytes(signature)
        run(['openssl','dgst','-sha256','-verify',str(ROOT/'ota/public-key.pem'),'-signature',str(b),str(a)])
    p=json.loads(raw)
    assert p['applicationId']==APP and p['channel']=='beta',path
    for f in p['files']:
        blob=ROOT/'ota/blobs'/(f['sha256']+'.bin')
        assert f['url']==ORIGIN+'blobs/'+blob.name,f
        assert len(blob.read_bytes())==f['size'] and hashlib.sha256(blob.read_bytes()).hexdigest()==f['sha256'],f
    return p
def main():
    d=ROOT/'beta-dist'
    checks=json.loads((d/'checksums.json').read_text())
    for name,c in checks.items():
        data=(d/name).read_bytes()
        assert len(data)==c['bytes'] and hashlib.sha256(data).hexdigest()==c['sha256'],name
    snapshots={}
    for version,revision in [('3.0',30000),('3.0.1',30001)]:
        manifest=d/('manifest-'+version+'.json')
        assert manifest.read_bytes()==(ROOT/'ota'/manifest.name).read_bytes()
        p=payload(manifest);snapshots[version]=p
        assert p['version']==version and p['revision']==revision
        apk=d/('slovoplet-beta-'+version+'.apk')
        badging=run([sdk_tool('aapt2'),'dump','badging',str(apk)])
        assert re.search("package: name='([^']+)'",badging)[1]==APP,apk
        assert "versionCode='"+str(revision)+"'" in badging and "versionName='"+version+"'" in badging,apk
        assert "minSdkVersion:'24'" in badging and 'android.permission.REQUEST_INSTALL_PACKAGES' not in badging
        assert "launchable-activity: name='com.iluhin.fiveletters.MainActivity'" in badging
        certificate=run([sdk_tool('apksigner'),'verify','--print-certs',str(apk)])
        assert CERT in certificate.replace(':','').lower(),apk
        with zipfile.ZipFile(apk) as z:
            dex=z.read('classes.dex')
            assert ORIGIN.encode() in dex and b'con.iluhin.fiveletters.beta' not in dex
            for f in p['files']:
                assert hashlib.sha256(z.read('assets/web/'+f['path'])).hexdigest()==f['sha256'],f
        with zipfile.ZipFile(d/('components-'+version+'.zip')) as z:
            assert z.read('manifest.json')==manifest.read_bytes()
            for f in p['files']:
                assert hashlib.sha256(z.read('web/'+f['path'])).hexdigest()==f['sha256'],f
    assert (ROOT/'ota/manifest.json').read_bytes()==(d/'manifest-3.0.1.json').read_bytes()
    assert payload(ROOT/'ota/manifest.json')['applicationId']==APP
    before={f['path']:f for f in snapshots['3.0']['files']}
    changed=[f for f in snapshots['3.0.1']['files'] if before[f['path']]['sha256']!=f['sha256']]
    assert len(changed)==1 and changed[0]['size']==152 and len(before)-len(changed)==9
    print('PASS com application ID, APK launch identity/versions, owner signatures, signed OTA origin, ZIP/APK component hashes and 152-byte update')
if __name__=='__main__':main()
