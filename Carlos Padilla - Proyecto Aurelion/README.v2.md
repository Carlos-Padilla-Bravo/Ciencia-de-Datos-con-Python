# Documentación Interactiva - Proyecto Aurelion

Este es un programa interactivo que permite navegar fácilmente por la documentación del Proyecto Aurelion directamente desde la terminal.

## Requisitos

- Python 3.x instalado

## Estructura de Archivos

```
Carlos Padilla - Proyecto Aurelion/
│
├── README.md                     # Este archivo
├── Documentación.md             # Documentación completa del proyecto en formato Markdown
├── documentacion_interactiva.py   # El programa interactivo para navegar la documentación
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
    python documentacion_interactiva.py
    ```

## Navegación

El programa leerá el archivo `Documentación.md` y te presentará un menú con las secciones principales del documento.

-   Usa los números que aparecen en el menú para seleccionar una sección o subsección.
-   Si una sección es muy larga, se mostrará paginada. Puedes usar `Enter` para ir a la página siguiente, `b` para la anterior y `q` para volver al menú.
-   Ingresa `0` para volver al menú anterior o para salir del programa desde el menú principal.

## Mantenimiento

La ventaja de esta nueva versión es que el contenido se carga dinámicamente desde `Documentación.md`.

-   **Para actualizar el contenido**, simplemente edita el archivo `Documentación.md`.
-   **Para cambiar la estructura**, asegúrate de seguir las convenciones de encabezados de Markdown (`#` para títulos principales y `##` para subtítulos). El programa se adaptará automáticamente a los cambios la próxima vez que lo ejecutes.
