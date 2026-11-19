# Beta-канал веб-компонентов

[Главная beta](../README.md) · [Проверить 3.0 → 3.0.1](../docs/TESTING.md) · [Архитектура](../wiki/Architecture.md)

Текущая версия компонентов — **3.0.1**, ревизия `30001`.
Совместимые сборки оболочки: `30000–39999`. Пакет: `con.iluhin.fiveletters.beta`.

| Файл | Роль |
|---|---|
| [manifest.json](manifest.json) | Текущий подписанный указатель канала |
| [manifest-3.0.json](manifest-3.0.json) | Исходный снимок |
| [manifest-3.0.1.json](manifest-3.0.1.json) | Снимок проверочного обновления |
| [blobs/](blobs/) | Компоненты с именами по SHA-256 |
| [public-key.pem](public-key.pem) | Открытый ключ для независимой проверки подписи |
| [checksums.json](checksums.json) | Контрольные суммы подготовленных файлов релизов |

## Адреса после переноса

Эта папка содержит точную копию подписанных снимков 3.0 / 3.0.1.
Копия доступна в main нового репозитория:

https://raw.githubusercontent.com/iluhin/app.slovoplet.beta/main/ota/manifest.json

Установленные APK 3.0 / 3.0.1 продолжают читать прежний канал:

https://raw.githubusercontent.com/iluhin/app.slovoplet/beta/ota/manifest.json

Адреса blobs внутри подписанного payload также прежние. Они сохранены вместе
с технической веткой, потому что старый загрузчик отвергает чужой origin и
перенаправления. Для самостоятельного канала по новому адресу понадобится
следующая APK-оболочка. [Подробности](../docs/MIGRATION.md).

## Манифест

Внешняя JSON-обёртка содержит два Base64-поля:

```json
{
  "payload": "<точные UTF-8-байты манифеста в Base64>",
  "signature": "<RSA/SHA-256-подпись этих байтов в Base64>"
}
```

После декодирования payload содержит:

| Поле | Значение для 3.0.1 |
|---|---|
| `format` | `1` |
| `channel` | `beta` |
| `applicationId` | `con.iluhin.fiveletters.beta` |
| `version` / `revision` | `3.0.1` / `30001` |
| `minShell` / `maxShell` | `30000` / `39999` |
| `files` | Полный набор из 10 файлов с `path`, `size`, `sha256`, `url` |

Ревизия вычисляется как `major × 10000 + minor × 100 + patch`; недостающий
patch равен нулю, каждая часть не больше 99. Это схема данного beta-загрузчика,
а не правило для прежних стабильных `versionCode`.

URL компонента имеет вид:

```text
https://raw.githubusercontent.com/iluhin/app.slovoplet/beta/ota/blobs/<sha256>.bin
```

Хеш в имени, хеш содержимого и хеш в подписанном payload должны совпасть.
Расширение `.bin` в URL не задаёт тип файла: путь назначения берётся из подписанного манифеста.

## Ограничения формата 1

- Только канал `beta` и запрошенный пакет приложения.
- Внешняя JSON-обёртка с Base64-полями — до 512 КиБ; от 5 до 256 файлов в payload.
- Один компонент — до 4 МиБ, весь набор — до 16 МиБ.
- Обязательны `index.html`, `assets/game.js`, `assets/game.css`, `assets/offline.js`, `app/seed.json`.
- Пути: `index.html`, файлы внутри `assets/`, `app/seed.json`. Только ASCII-символы
  из `[A-Za-z0-9_./-]+`, максимум 180 символов; без абсолютных путей, `//`,
  скрытых сегментов, обхода `..` и повторяющихся имён. Например, `assets/icon.png`
  допустим, а `assets/иконка.png` — нет.
- Разрешённые расширения: `html`, `js`, `css`, `json`, `svg`, `png`, `jpg`, `jpeg`, `webp`, `woff`, `woff2`.
- URL — в закреплённом каталоге beta-канала. Более старая или уже установленная
  ревизия не применяется, неудачная ревизия блокируется.

Манифест перечисляет полный снимок. Для демонстрации отличаются только байты
`assets/beta-release.json`: загрузчик получает **152 байта компонента** и
переиспользует девять файлов. Подписанный манифест передаётся отдельно.

## Проверка подписи вручную

Нужны Python 3 и OpenSSL. Команды выполняются из корня этого репозитория:

```bash
python3 - <<'PY'
import base64, json, pathlib, tempfile, subprocess
root = pathlib.Path('ota')
envelope = json.loads((root / 'manifest.json').read_text())
with tempfile.TemporaryDirectory() as directory:
    payload = pathlib.Path(directory) / 'payload.json'
    signature = pathlib.Path(directory) / 'signature.bin'
    payload.write_bytes(base64.b64decode(envelope['payload'], validate=True))
    signature.write_bytes(base64.b64decode(envelope['signature'], validate=True))
    subprocess.run(['openssl', 'dgst', '-sha256', '-verify', str(root / 'public-key.pem'),
                    '-signature', str(signature), str(payload)], check=True)
    print(json.dumps(json.loads(payload.read_text()), ensure_ascii=False, indent=2))
PY
```

Ожидается `Verified OK`, затем содержимое payload. Это проверка файла открытым
ключом из репозитория. Приложение использует ключ, уже закреплённый в APK: замена PEM
в репозитории не заменяет ключ на телефоне.

[Подготовка следующего выпуска →](../docs/RELEASING.md) · [Подтверждённые проверки →](../docs/VERIFICATION.md)
