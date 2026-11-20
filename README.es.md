[Русский](README.md) · [English](README.en.md) · **Español** · [简体中文](README.zh-CN.md)

> **Corrección 3.1.1:** el APK 3.1 falla al iniciar por una llamada a una API no pública de accesos directos de Android. Instala el APK 3.1.1 sobre la beta, sin desinstalar ni borrar datos. Una actualización OTA de componentes no corrige el código nativo.

<div align="center">

<img src="cover.png" alt="Slovoplet Beta">

</div>

# Slovoplet · Beta 3.1.1

**Widgets de inicio, accesos directos dinámicos y actualizaciones por componentes.**
La beta 3.1.1 incorpora las funciones previstas para la versión estable 2.8.
Los canales estable y beta tienen numeraciones independientes.

[**Probar OTA a 3.1.1**](docs/TESTING.md) ·
[**APK 3.1.1 — widgets**](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.1.1/slovoplet-beta-3.1.1.apk) ·
[**Versiones beta**](releases/README.md) ·
[**Juego estable**](https://github.com/iluhin/app.slovoplet)

## Dos partes de esta versión

| Parte | Versión | Cómo obtenerla |
|---|---|---|
| Componentes web | **3.1.1**, revisión **30101** | Desde la beta corregida 3.0 / 3.0.1 ya instalada |
| Contenedor de Android | **3.1.1**, compilación **30101** | Instalar el APK 3.1.1 sobre la beta com corregida |
| Identificador | **com.iluhin.fiveletters.beta** | Se conserva el certificado del propietario |

**Para probar OTA, no instales primero el APK 3.1.1.** Abre la beta 3.0 / 3.0.1,
pulsa el botón beta inferior y busca actualizaciones. Termina la partida y aplica
los componentes descargados. El resultado debe ser:
**contenedor APK 3.0 (o 3.0.1) · componentes 3.1.1**, sin el instalador de Android.

APK inicial, si lo necesitas: [3.0 r2](https://github.com/iluhin/app.slovoplet.beta/releases/download/beta-v3.0.0-r2/slovoplet-beta-3.0.apk).
Después puedes instalar el APK 3.1.1 sobre la beta corregida: mantiene el
identificador y el certificado, por lo que no hace falta desinstalarla.

## Funciones del plan 2.8

- **Estadísticas**: partidas, victorias, porcentaje de victorias, racha y mejor tiempo; distribución de intentos en el widget ancho.
- **Palabra del día**: estado y tiempo aproximado hasta el nuevo día en Moscú.
- **Inicio rápido**: nueva partida o continuar, con cinco casillas de colores del último resultado y sin letras.
- **Clasificación**: tres líderes, tu posición conocida y fecha de la captura.
- **Accesos directos dinámicos**: nueva/continuar, palabra del día, clasificación y perfil.
- **Vista previa dentro del juego**: llega con los componentes 3.1.1, también en los contenedores anteriores.

Los widgets reales del escritorio y los accesos directos requieren **APK 3.1.1**.
Actualizar archivos web no añade clases Java ni recursos Android. Los widgets
funcionan desde Android 7.0; los accesos dinámicos requieren Android 7.1 y un
lanzador compatible. [Configuración y funcionamiento →](docs/WIDGETS.md)

## Actualizaciones y datos

El manifiesto firmado con RSA/SHA-256 describe todos los archivos. Solo se
descargan los componentes modificados y se aplican tras la partida o al volver
a iniciar la aplicación. La confirmación del inicio y la reversión protegen la
versión funcional. Contenedor, componentes y sitio muestran versiones separadas.

Los widgets guardan una captura local y funcionan sin conexión. La clasificación
se actualiza durante el uso real del juego, con solicitudes adicionales limitadas
a una cada 30 minutos. La aplicación cerrada no hace consultas de fondo, evitando
una presencia en línea y estadísticas de visitas falsas. Se muestra la fecha de los datos.
El contador diario usa Europe/Moscow. Android puede retrasar la actualización
del widget, prevista aproximadamente cada 30 minutos.

La beta comparte el servidor del juego. Los datos locales están separados,
pero el mismo nombre de usuario abre el mismo perfil del servidor.

## Documentación

[Historial](CHANGELOG.md) · [Plan](ROADMAP.md) · [Prueba OTA](docs/TESTING.md) ·
[Widgets](docs/WIDGETS.md) · [Comprobaciones y límites](docs/VERIFICATION.md) ·
[Formato OTA](ota/README.md) · [Publicación](docs/RELEASING.md) ·
[Informar de un problema](CONTRIBUTING.md) · [Guía](wiki/Home.md)

Las guías enlazadas y los botones del juego están en ruso. Este repositorio público
contiene documentación y compilaciones preparadas; el código fuente principal
se guarda por separado. Se conserva la clave de firma del propietario.
Las antiguas compilaciones con el paquete con son aplicaciones distintas:
[instrucciones de migración](docs/MIGRATION.md).

El informe detalla las comprobaciones automáticas y sus límites. Las pruebas
de instalación, colocación de widgets, lanzador y batería en un dispositivo
Android real esperan comentarios de quienes prueban la beta.

---
© Ilya Anisimov · [iluh.in](https://iluh.in)
