[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · **简体中文**

<div align="center">

<img src="cover.png" alt="Slovoplet Beta">

</div>

# Slovoplet · Beta 3.1

**桌面小组件、动态快捷方式和组件更新。**
Beta 3.1 引入了稳定版 2.8 计划中的功能。稳定渠道与 beta 渠道分别编号。

[**测试 OTA 更新到 3.1**](docs/TESTING.md) ·
[**APK 3.1 — 小组件**](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.1.0/slovoplet-beta-3.1.apk) ·
[**Beta 发布版本**](releases/README.md) ·
[**稳定版游戏**](https://github.com/iluhin/app.slovoplet)

## 本次发布的两个部分

| 部分 | 版本 | 获取方式 |
|---|---|---|
| Web 组件 | **3.1**，修订号 **30100** | 在已安装的修正版 beta 3.0 / 3.0.1 内更新 |
| Android 原生外壳 | **3.1**，构建号 **30100** | 在修正后的 com beta 上安装 APK 3.1 |
| 应用 ID | **com.iluhin.fiveletters.beta** | 保留所有者原有的签名证书 |

**测试 OTA 时，请勿先安装 APK 3.1。** 打开已安装的 beta 3.0 / 3.0.1，
点击底部 beta 按钮并检查更新。完成本局后应用下载的组件。
预期结果：**APK 外壳 3.0（或 3.0.1）· 组件 3.1**，不会打开 Android 安装程序。

需要初始 APK 时，可下载 [3.0 r2](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.0.0-r2/slovoplet-beta-3.0.apk)。
完成组件测试后，可在修正版 beta 上安装 APK 3.1；
应用 ID 和证书相同，无需卸载修正版应用。

## 从 2.8 计划引入的功能

- **统计小组件**：游戏次数、胜场、连胜、最佳用时；加宽后显示各尝试次数的胜场分布。
- **每日单词**：完成状态及距离莫斯科新一天的大致时间。
- **快速开始**：新游戏或继续游戏，仅显示上一局的五个彩色方格，不显示字母。
- **排行榜**：前三名、已知的个人名次以及数据保存时间。
- **动态快捷方式**：新建/继续、每日单词、排行榜和个人资料。
- **游戏内小组件预览**：随组件 3.1 更新到旧版外壳上。

真正的桌面小组件和快捷方式需要 **APK 3.1**。
Web 文件更新无法增加 Java 类或 Android 资源。小组件支持 Android 7.0 及以上；
动态快捷方式需要 Android 7.1 及兼容的桌面启动器。
[设置与使用说明 →](docs/WIDGETS.md)

## 更新与数据

RSA/SHA-256 签名清单描述完整文件集合，只下载已变更的组件。
更新在本局结束后或重新启动时应用。启动确认和回滚保护可用版本，
原生外壳、组件和网站的版本分别显示。

小组件保存本地快照，可离线显示。排行榜仅在实际使用游戏时刷新，
额外请求最多每 30 分钟一次。游戏关闭后不进行后台请求，
避免造成虚假的在线状态和访问统计。小组件会标明数据保存时间。
每日时间按 Europe/Moscow 计算；约每 30 分钟一次的系统刷新可能被 Android 延迟。

Beta 与常规版共用游戏服务器。本地数据相互独立，
使用相同用户名登录时会打开同一个服务器个人资料。

## 文档

[更新记录](CHANGELOG.md) · [开发计划](ROADMAP.md) · [OTA 测试](docs/TESTING.md) ·
[小组件](docs/WIDGETS.md) · [检查结果与限制](docs/VERIFICATION.md) ·
[OTA 格式](ota/README.md) · [发布流程](docs/RELEASING.md) ·
[报告问题](CONTRIBUTING.md) · [指南](wiki/Home.md)

链接中的指南和游戏按钮目前使用俄语。本公开仓库保存文档和已准备的构建，
主要源代码另行保存。APK 继续使用所有者原有的签名密钥。
旧的错误 con 包属于另一应用：[迁移说明](docs/MIGRATION.md)。

验证报告说明了自动检查及其适用范围。
真机安装、小组件放置、启动器行为和耗电情况仍待测试者反馈。

---
© Ilya Anisimov · [iluh.in](https://iluh.in)
