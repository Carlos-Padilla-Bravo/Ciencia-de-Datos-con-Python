# Documentación Interactiva - Proyecto Aurelion

Este es un programa interactivo que permite navegar fácilmente por la documentación del Proyecto Aurelion directamente desde la terminal.

## Requisitos

- Python 3.x instalado

## Estructura de Archivos

```
Carlos Padilla - Proyecto Aurelion/
│
├── README.v2.md                     # Este archivo
├── Documentación-v2.md             # Documentación completa del proyecto en formato Markdown
├── documentacion_interactiva-v2.py   # El programa interactivo para navegar la documentación
├── clientes.xlsx                # Base de datos de clientes
├── productos.xlsx               # Base de datos de productos
├── ventas.xlsx                 # Base de datos de ventas
└── detalle_ventas.xlsx         # Base de datos de detalle de ventas
```

## Cómo Usar el Programa

1.  Abre una terminal (como `cmd`, `PowerShell` o la terminal de Visual Studio Code).
2.  Navega hasta la carpeta donde se encuentra el proyecto.
    ```sh
    cd "ruta\a\la\carpeta\Carlos Padilla - Proyecto Aurelion"
    ```
3.  Ejecuta el programa con el siguiente comando:
    ```sh
    python documentacion_interactiva-v2.py
    ```

## Navegación

El programa leerá el archivo `Documentación-v2.md` y te presentará un menú con las secciones principales del documento.

-   Usa los números que aparecen en el menú para seleccionar una sección o subsección.
-   Si una sección es muy larga, se mostrará paginada. Puedes usar `Enter` para ir a la página siguiente, `b` para la anterior y `q` para volver al menú.
-   Ingresa `0` para volver al menú anterior o para salir del programa desde el menú principal.

## Visualización de Figuras

Al navegar por el programa notarás que hay links a Figuras. Para visualizar las figuras incluidas en la documentación debes hacer lo siguiente:

- Debes cargar en tu workspace de VSCode la carpeta Figuras
- Copiar el nombre de la figura que deseas visualizar (el nombre de la Figura está entre corchetes).
- Tecla Ctrl + clic sobre el enlace de la figura en la terminal.
- Se abrirá una ventana en la cual debes pegar el nombre de la figura copiada.
- Presiona Enter o haz clic en el nombre de la figura que se despliega en la ventana.
- La figura se desplegará en VSCode.
- Puedes hacer zoom para una mejor visualización si es necesario.

## Mantenimiento

La ventaja de esta nueva versión es que el contenido se carga dinámicamente desde `Documentación-v2.md`.

-   **Para actualizar el contenido**, simplemente edita el archivo `Documentación-v2.md`.
-   **Para cambiar la estructura**, asegúrate de seguir las convenciones de encabezados de Markdown (`#` para títulos principales y `##` para subtítulos). El programa se adaptará automáticamente a los cambios la próxima vez que lo ejecutes.
