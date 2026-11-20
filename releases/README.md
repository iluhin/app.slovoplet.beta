# Выпуски beta

[Главная beta](../README.md) · [История](../CHANGELOG.md) · [Сценарий проверки](../docs/TESTING.md)

| Выпуск | Что устанавливать | Для чего |
|---|---|---|
| [3.0 beta](https://github.com/iluhin/app.slovoplet.beta/releases/tag/beta-v3.0.0-r2) | [APK 3.0](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.0.0-r2/slovoplet-beta-3.0.apk) | Начальная установка и проверка OTA |
| [3.0.1 beta](https://github.com/iluhin/app.slovoplet.beta/releases/tag/beta-v3.0.1-r2) | Компоненты предлагает сама beta 3.0 | Проверочный переход без переустановки APK |

У 3.0.1 есть контрольный APK для чистой установки. Он не нужен для проверки
перехода с 3.0. В каждом выпуске также доступны подписанный снимок манифеста,
контрольные суммы и ZIP веб-компонентов для просмотра.

## Каналы и теги

- `beta-v3.0.0-r2`, `beta-v3.0.1-r2` — предварительные beta-релизы, `prerelease=true`.
- `v2.7.2` и прежние `v*` — стабильная история, не beta-сборки.
- [Latest](https://github.com/iluhin/app.slovoplet/releases/latest) остаётся стабильным выпуском.

[Порядок публикации](../docs/RELEASING.md) объясняет роль `beta-dist/` и workflow.

## Стабильный архив

Стабильные версии 1.4–2.7.2, их APK и подробные заметки находятся
в [основном репозитории](https://github.com/iluhin/app.slovoplet/releases).
Они не дублируются в отдельном beta-пространстве.

## Исправление идентификатора

Актуальны исправленные сборки r2 с пакетом com.iluhin.fiveletters.beta.
Они используют независимый OTA-канал этого репозитория.
Первоначальные ошибочные сборки убраны из списка актуальных выпусков.
[Переход и подпись](../docs/MIGRATION.md).
