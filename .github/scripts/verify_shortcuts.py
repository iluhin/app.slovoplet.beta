"""Regression: packaged APK must call the public CharSequence overload, never hidden String."""
import struct,sys,zipfile

def shortcut_disable_prototypes(dex):
    def u32(at): return struct.unpack_from('<I',dex,at)[0]
    count,offset=struct.unpack_from('<II',dex,56)
    strings=[]
    for i in range(count):
        at=u32(offset+4*i)
        while dex[at]&128: at+=1
        at+=1
        strings.append(dex[at:dex.index(0,at)].decode('utf-8','replace'))
    count,offset=struct.unpack_from('<II',dex,64)
    types=[strings[u32(offset+4*i)] for i in range(count)]
    count,offset=struct.unpack_from('<II',dex,72)
    prototypes=[]
    for i in range(count):
        _,ret,params=struct.unpack_from('<III',dex,offset+12*i)
        args=[] if not params else [types[struct.unpack_from('<H',dex,params+4+2*j)[0]] for j in range(u32(params))]
        prototypes.append('('+''.join(args)+')'+types[ret])
    count,offset=struct.unpack_from('<II',dex,88)
    found=[]
    for i in range(count):
        cls,proto,name=struct.unpack_from('<HHI',dex,offset+8*i)
        if types[cls]=='Landroid/content/pm/ShortcutManager;' and strings[name]=='disableShortcuts': found.append(prototypes[proto])
    return found

def verify(apk):
    with zipfile.ZipFile(apk) as z: actual=shortcut_disable_prototypes(z.read('classes.dex'))
    expected=['(Ljava/util/List;Ljava/lang/CharSequence;)V']
    assert actual==expected, f'Non-public Android shortcut overload in {apk}: {actual}; expected {expected}'
    print('PASS public Android disableShortcuts(List, CharSequence) in packaged APK')

if __name__=='__main__':verify(sys.argv[1])
