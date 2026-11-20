[Русский](README.md) · **English** · [Español](README.es.md) · [简体中文](README.zh-CN.md)

<div align="center">

<img src="cover.png" alt="Slovoplet Beta">

</div>

# Slovoplet · Beta 3.1

**Home-screen widgets, dynamic shortcuts and component updates.**
Beta 3.1 brings the features planned for stable version 2.8 into the beta channel.
Stable and beta releases have separate version sequences.

[**Test OTA to 3.1**](docs/TESTING.md) ·
[**APK 3.1 — widgets**](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.1.0/slovoplet-beta-3.1.apk) ·
[**Beta releases**](releases/README.md) ·
[**Stable game**](https://github.com/iluhin/app.slovoplet)

## Two parts of this release

| Part | Version | How to get it |
|---|---|---|
| Web components | **3.1**, revision **30100** | Inside the installed corrected beta 3.0 / 3.0.1 |
| Android shell | **3.1**, build **30100** | Install APK 3.1 over the corrected com beta |
| Application ID | **com.iluhin.fiveletters.beta** | The owner's signing certificate is unchanged |

**To test OTA, do not install APK 3.1 first.** Open the installed beta 3.0 / 3.0.1,
tap the beta button at the bottom and check for updates. Finish the current round
and apply the downloaded components. The result is:
**APK shell 3.0 (or 3.0.1) · components 3.1**, without the Android installer.

If you need a starting APK: [3.0 r2](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.0.0-r2/slovoplet-beta-3.0.apk).
After testing the components, you can install APK 3.1 over the corrected beta:
its application ID and signing certificate are the same, so uninstalling is unnecessary.

## Features from the 2.8 plan

- **Statistics**: games, wins, win percentage, streak and best time; attempt distribution in the wider widget.
- **Daily word**: completion status and approximate time until the next day in Moscow.
- **Quick start**: a new game or continuation, with five colored tiles from the last round and no letters.
- **Leaderboard**: three leaders, your known position and the snapshot date.
- **Dynamic shortcuts**: new/continue, daily word, leaderboard and profile.
- **In-game widget preview**: delivered with components 3.1, including on older shells.

Actual home-screen widgets and shortcuts require **APK 3.1**. Web file updates
cannot add Java classes or Android resources. Widgets support Android 7.0+;
dynamic shortcuts require Android 7.1+ and a compatible launcher.
[Widget setup and behavior →](docs/WIDGETS.md)

## Updates and data

The RSA/SHA-256 signed manifest describes the complete file set. Only changed
components are downloaded. They are applied after a round or on a fresh launch,
with startup confirmation and rollback protecting the working version.
Shell, component and website versions are displayed separately.

Widgets use a saved local snapshot and work offline. Leaderboard data refreshes
during real foreground use, with extra requests limited to once every 30 minutes.
A closed app makes no background requests, avoiding false online presence and
visit statistics. The widget displays the snapshot date.
The daily countdown uses Europe/Moscow. Android may delay the approximately
30-minute system widget refresh.

Beta uses the shared game server. The apps have separate local data, but signing
in with the same username opens the same server profile.

## Documentation

[Changelog](CHANGELOG.md) · [Roadmap](ROADMAP.md) · [OTA test](docs/TESTING.md) ·
[Widgets](docs/WIDGETS.md) · [Checks and limitations](docs/VERIFICATION.md) ·
[OTA format](ota/README.md) · [Release procedure](docs/RELEASING.md) ·
[Report a problem](CONTRIBUTING.md) · [Guide](wiki/Home.md)

Linked documentation and in-app labels are in Russian. This public repository
contains documentation and prepared builds; the main source code is kept separately.
APKs use the owner's existing signing key. Old misspelled con builds are separate
applications: [migration instructions](docs/MIGRATION.md).

The verification report describes automated checks and their limits. Testing
installation, widget placement, launcher behavior and battery use on a real
Android device is awaiting tester feedback.

---
© Ilya Anisimov · [iluh.in](https://iluh.in)
