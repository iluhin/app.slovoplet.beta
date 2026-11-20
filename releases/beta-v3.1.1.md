# 3.1.1 beta — исправлен вылет при запуске

В APK 3.1 попала непубличная перегрузка Android ShortcutManager.disableShortcuts(List, String).
При запуске Android выбрасывал NoSuchMethodError и закрывал игру.

Сборка 3.1.1 использует публичный метод с CharSequence и официальный Android SDK 34.
Добавлена проверка сигнатуры метода в готовом APK.

**Для восстановления установите slovoplet-beta-3.1.1.apk поверх текущей beta.**
Не удаляйте приложение и не очищайте данные. Пакет com.iluhin.fiveletters.beta,
прежний сертификат владельца; versionCode 30101, версия 3.1.1.
Одно OTA компонентов не может исправить этот сбой нативного кода.
Четыре виджета и шорткаты из 3.1 сохранены, часовой пояс — Europe/Moscow.

Ошибка воспроизведена запуском опубликованного 3.1 на эмуляторе Android 9 / API 28.
Исправленный APK проверен установкой поверх 3.1 с сохранением контрольного файла данных
и тремя холодными запусками без FATAL EXCEPTION.
Проверка на Pixel 9 Pro / Android 17 остаётся за владельцем устройства.

Файлы: APK, полный ZIP компонентов, подписанный manifest и SHA-256 checksums.
Прежние APK и снимки сохранены; текущий OTA-канал содержит компоненты 3.1.1.

[Восстановление](https://github.com/iluhin/app.slovoplet.beta/blob/main/docs/TESTING.md) ·
[Проверки](https://github.com/iluhin/app.slovoplet.beta/blob/main/docs/VERIFICATION.md)
