# Documentación Interactiva - Proyecto Aurelion

Este es un programa interactivo que permite navegar fácilmente por la documentación del Proyecto Aurelion.

## Requisitos

- Python 3.x instalado
- Visual Studio Code
- Tener todos los archivos del proyecto en la misma carpeta

## Estructura de Archivos

```
Carlos Padilla - Proyecto Aurelion/
│
├── README.md               # Este archivo
├── Documentación.md       # Documentación completa del proyecto
├── doc_interactiva.py     # Programa interactivo para navegar la documentación
├── paginador.py          # Módulo auxiliar para la visualización paginada
├── clientes.xlsx          # Base de datos de clientes
├── productos.xlsx         # Base de datos de productos
├── ventas.xlsx           # Base de datos de ventas
└── detalle_ventas.xlsx   # Base de datos de detalle de ventas
```

## Cómo Usar el Programa

1. Abre Visual Studio Code
2. Abre la carpeta del proyecto ("Tu nombre - Proyecto Aurelion")
3. Abre una terminal en VS Code (Menú Ver > Terminal)
4. Ejecuta el programa con el comando:
   ```
   python doc_interactiva.py
   ```

## Navegación

El programa ofrece un menú interactivo con las siguientes secciones:

1. Proyecto Aurelion
2. Creación de carpeta en PC y descarga de archivos
3. Descripción de las tablas xlsx
4. Definición del problema y solución
5. Diagrama de flujo
6. Pseudocódigo

- Usa los números (0-6) para navegar por las secciones
- Presiona 0 para volver al menú anterior o salir
- Sigue las instrucciones en pantalla

## Solución de Problemas

Si encuentras algún error al ejecutar el programa:

1. Asegúrate de estar en la carpeta correcta del proyecto
2. Verifica que Python esté instalado ejecutando `python --version` en la terminal
3. Comprueba que todos los archivos estén en la misma carpeta

Si el problema persiste, revisa el código fuente para identificar posibles errores.