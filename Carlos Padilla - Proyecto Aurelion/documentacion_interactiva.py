import os
import time
from typing import Dict, List

class DocumentacionInteractiva:
    def __init__(self):
        self.secciones = {
            1: "Proyecto Aurelion",
            2: "Creación de carpeta en PC y descarga de archivos",
            3: "Descripción de las tablas xlsx",
            4: "Definición del problema y solución",
            5: "Diagrama de flujo",
            6: "Pseudocódigo"
        }
        
        self.subsecciones = {
            3: {
                1: "Base de datos clientes",
                2: "Base de datos de productos",
                3: "Base de datos de ventas",
                4: "Base de datos detalle_ventas"
            },
            4: {
                1: "Problema",
                2: "Solución",
                3: "Supuestos y reglas",
                4: "KPIs principales"
            }
        }

    def limpiar_pantalla(self):
        """Limpia la pantalla de la terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_texto_paginado(self, texto: str):
        """Muestra texto largo con paginación y navegación mejorada."""
        lineas = texto.split('\n')
        alto_terminal = os.get_terminal_size().lines - 4  # Dejamos espacio para el menú
        total_paginas = (len(lineas) + alto_terminal - 1) // alto_terminal
        pagina_actual = 0

        while pagina_actual < total_paginas:
            self.limpiar_pantalla()
            inicio = pagina_actual * alto_terminal
            fin = min((pagina_actual + 1) * alto_terminal, len(lineas))
            
            # Mostrar el contenido de la página actual
            print('\n'.join(lineas[inicio:fin]))
            
            # Mostrar menú de navegación
            if total_paginas > 1:
                print("\n" + "=" * 50)
                print(f"Página {pagina_actual + 1} de {total_paginas}")
                if pagina_actual < total_paginas - 1:
                    print("Presione:")
                    print("- ENTER para siguiente página")
                    print("- 'b' para página anterior")
                    print("- 'q' para volver al menú")
                else:
                    print("Presione:")
                    print("- 'b' para página anterior")
                    print("- ENTER o 'q' para volver al menú")
                
                respuesta = input("\nOpción: ").lower()
                if respuesta == 'q':
                    break
                elif respuesta == 'b' and pagina_actual > 0:
                    pagina_actual -= 1
                elif respuesta == '' and pagina_actual < total_paginas - 1:
                    pagina_actual += 1
                elif pagina_actual == total_paginas - 1:
                    break
            else:
                input("\nPresione Enter para volver al menú...")
                break

    def mostrar_menu_principal(self):
        """Muestra y gestiona el menú principal."""
        while True:
            self.limpiar_pantalla()
            print("\n=== DOCUMENTACIÓN PROYECTO AURELION ===")
            print("\nSecciones disponibles:")
            for num, seccion in self.secciones.items():
                print(f"{num}. {seccion}")
            print("0. Salir")
            
            try:
                opcion = int(input("\nSeleccione una sección (0-6): "))
                if opcion == 0:
                    print("\n¡Gracias por usar la documentación interactiva!")
                    print("Presione Enter para salir...")
                    input()
                    break
                elif opcion in self.secciones:
                    self.mostrar_seccion(opcion)
                else:
                    print("\nOpción no válida. Por favor, intente nuevamente.")
                    time.sleep(1)
            except ValueError:
                print("\nPor favor, ingrese un número válido.")
                time.sleep(1)

    def mostrar_seccion(self, numero_seccion: int):
        """Muestra el contenido de una sección específica."""
        self.limpiar_pantalla()
        print(f"\n=== {self.secciones[numero_seccion]} ===\n")
        
        if numero_seccion == 1:
            contenido = """En el marco del curso sobre Fudamentos de Inteligencia Ariticial impartido por Guayer
en conjunto con IBM se pretende desarrollar un programa en Python para dar
cumplimiento con los requisitos del curso. Para tal fin se utilizarán distintas
tablas de datos relacionadas con ventas de productos alimenticios y de limpieza."""
            self.mostrar_texto_paginado(contenido)

        elif numero_seccion == 2:
            contenido = """Para desarrollar el Proyecto Aurelion se siguieron los primeros pasos iniciales:

- Creación de carpeta en PC con el nombre de Carlos Padilla-Proyecto Aurelion
- Descarga de archivos con extensión xlss desde Google Drive (4 archivos)
- Conexión carpeta con Visual Studio Code (Add Folder to Workspace)
- Inspección inicial de cada archivo en VSC para conocer su contenido
- Creación de un archivo md para documentar el proyecto"""
            self.mostrar_texto_paginado(contenido)

        elif numero_seccion in [3, 4]:
            self.mostrar_submenu(numero_seccion)
            return

        elif numero_seccion == 5:
            diagrama_flujo = """[Inicio: Comienza el Proceso del Proyecto Aurelion]
    |
    V
[Datos: Cargar 4 archivos XLSX en DataFrames de Pandas]
    |-> (clientes.xlsx -> df_clientes)
    |-> (productos.xlsx -> df_productos)
    |-> (ventas.xlsx -> df_ventas)
    |-> (detalle_ventas.xlsx -> df_detalle_ventas)
    |
    V
[Proceso: Análisis Exploratorio de Datos (EDA) Inicial]
    |-> (Inspeccionar .head(), .info(), .describe() de cada DataFrame)
    |
    V
[Proceso: Limpieza de Datos y Validación]
    |
    |--- 1. Tabla 'productos'
    |      |-> [Proceso: Crear columna 'categoria_std' corrigiendo categorías]
    |      '-> [Proceso: Verificar duplicados en 'nombre_producto']
    |
    |--- 2. Tabla 'clientes'
    |      '-> [Proceso: Verificar duplicados en 'nombre_cliente' y 'email']
    |
    |--- 3. Tabla 'detalle_ventas' (Validación de Calidad)
    |      |-> [Proceso: Calcular 'importe_calculado' = cantidad * precio_unitario]
    |      |-> <Decisión: ¿Hay discrepancias?>
    |            |
    |            |--- (SI) ---> [Proceso: Reemplazar y registrar]
    |            |
    |            '--- (NO) ---> [Continuar]
    |
    V
[Proceso: Integración de Datos (Merges)]
    |-> [Unir tablas para crear vista consolidada]
    |-> [Validar integridad de datos]
    |
    V
[Proceso: Cálculo de KPIs]
    |
    |--- [Cálculo: Métricas de clientes]
    |--- [Cálculo: Métricas de ventas]
    |--- [Cálculo: Análisis por categoría]
    |--- [Cálculo: Análisis por ciudad]
    |
    V
[Salida: Resultados]
    |-> [KPIs en consola]
    |-> [Reportes en CSV]
    |
    V
[Fin]"""
            self.mostrar_texto_paginado(diagrama_flujo)

        elif numero_seccion == 6:
            pseudocodigo = """INICIO_PROGRAMA

// -----------------------------------------------------
// FASE 1: CARGA Y PREPARACIÓN DE DATOS
// -----------------------------------------------------
df_clientes = CARGAR_EXCEL("clientes.xlsx")
df_productos = CARGAR_EXCEL("productos.xlsx")
df_ventas = CARGAR_EXCEL("ventas.xlsx")
df_detalle_ventas = CARGAR_EXCEL("detalle_ventas.xlsx")

// Crear copias de respaldo
df_clientes_orig = COPIAR(df_clientes)
df_productos_orig = COPIAR(df_productos)
df_ventas_orig = COPIAR(df_ventas)
df_detalle_ventas_orig = COPIAR(df_detalle_ventas)

// -----------------------------------------------------
// FASE 2: ANÁLISIS EXPLORATORIO DE DATOS (EDA)
// -----------------------------------------------------
PARA CADA DataFrame EN [df_clientes, df_productos, df_ventas, df_detalle_ventas]:
    MOSTRAR_INFO(DataFrame)
    MOSTRAR_ESTADISTICAS(DataFrame)
    VERIFICAR_NULOS(DataFrame)
FIN PARA

// -----------------------------------------------------
// FASE 3: LIMPIEZA Y VALIDACIÓN
// -----------------------------------------------------
// Verificar duplicados
VERIFICAR_DUPLICADOS(df_clientes, ['email'])
VERIFICAR_DUPLICADOS(df_productos, ['nombre_producto'])

// Corregir categorías
PARA CADA producto EN df_productos:
    SI producto.categoria NO ES_CORRECTA:
        CORREGIR_CATEGORIA(producto)
        REGISTRAR_CAMBIO()
FIN PARA

// Validar importes
PARA CADA venta EN df_detalle_ventas:
    importe_calculado = venta.cantidad * venta.precio_unitario
    SI importe_calculado != venta.importe:
        CORREGIR_IMPORTE(venta, importe_calculado)
        REGISTRAR_ERROR()
FIN PARA

// -----------------------------------------------------
// FASE 4: INTEGRACIÓN
// -----------------------------------------------------
df_consolidado = UNIR_TABLAS([df_ventas, df_detalle_ventas, df_productos, df_clientes])

// -----------------------------------------------------
// FASE 5: CÁLCULO DE KPIS
// -----------------------------------------------------
total_clientes = CONTAR(df_clientes)
clientes_activos = CONTAR(DISTINTOS(df_consolidado.id_cliente))
ventas_totales = SUMA(df_consolidado.importe)
ventas_por_categoria = AGRUPAR_Y_SUMAR(df_consolidado, 'categoria')
ventas_por_ciudad = AGRUPAR_Y_SUMAR(df_consolidado, 'ciudad')

// -----------------------------------------------------
// FASE 6: REPORTES
// -----------------------------------------------------
GENERAR_REPORTE_GENERAL()
EXPORTAR_RESULTADOS_CSV()

FIN_PROGRAMA"""
            self.mostrar_texto_paginado(pseudocodigo)

    def mostrar_submenu(self, seccion_principal: int):
        """Muestra y gestiona los submenús de las secciones."""
        while True:
            self.limpiar_pantalla()
            print(f"\n=== {self.secciones[seccion_principal]} - Subsecciones ===\n")
            
            for num, subseccion in self.subsecciones[seccion_principal].items():
                print(f"{num}. {subseccion}")
            print("0. Volver al menú principal")
            
            try:
                opcion = int(input(f"\nSeleccione una subsección (0-{len(self.subsecciones[seccion_principal])}): "))
                if opcion == 0:
                    break
                elif opcion in self.subsecciones[seccion_principal]:
                    self.mostrar_subseccion(seccion_principal, opcion)
                else:
                    print("\nOpción no válida. Por favor, intente nuevamente.")
                    time.sleep(1)
            except ValueError:
                print("\nPor favor, ingrese solo números.")
                time.sleep(1)

    def mostrar_subseccion(self, seccion_principal: int, subseccion: int):
        """Muestra el contenido de una subsección específica."""
        self.limpiar_pantalla()
        print(f"\n=== {self.subsecciones[seccion_principal][subseccion]} ===\n")

        if seccion_principal == 3:  # Descripción de las tablas xlsx
            if subseccion == 1:  # Base de datos clientes
                contenido = """- Nombre de la BBDD: clientes
- Cantidad de columnas: 5 columnas
- Cantidad de observaciones (filas): 100 observaciones o registros
- Archivo con extensión xlsx

Variables:
1. id_cliente: cuantitativo (int), discreto, estructurado, intervalo
2. nombre_cliente: cualitativo (string), categórico, no estructurado, nominal
3. email: cualitativo (string), categórico, no estructurado, nominal
4. ciudad: cualitativo (string), categórico, no estructurado, nominal
5. fecha_alta: cuantitativo (formato fecha yy-mm-dd), discreto, estructurado, intervalo"""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 2:  # Base de datos de productos
                contenido = """- Nombre de la BBDD: productos
- Cantidad de columnas: 4 columnas
- Cantidad de observaciones (filas): 100 observaciones o registros
- Archivo con extensión xlsx

Variables:
1. id_producto: cuantitativo (int), discreto, estructurado, intervalo
2. nombre_producto: cualitativo (string), categórico, no estructurado, nominal
3. categoria: cualitativo (string), categórico, no estructurado, nominal
4. precio_unitario: cuantitativo (int), continuo, estructurado, razón"""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 3:  # Base de datos de ventas
                contenido = """- Nombre de la BBDD: ventas
- Cantidad de columnas: 6 columnas
- Cantidad de observaciones (filas): 120 observaciones o registros
- Archivo con extensión xlsx

Variables:
1. id_venta: cuantitativo (int), discreto, estructurado, intervalo
2. fecha: cuantitativo (formato fecha yy-mm-dd), discreto, estructurado, intervalo
3. id_cliente: cuantitativo (int), discreto, estructurado, intervalo
4. nombre_cliente: cualitativo (string), categórico, no estructurado, nominal
5. email: cualitativo (string), categórico, no estructurado, nominal
6. medio_pago: cualitativo (string), categórico, no estructurado, nominal"""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 4:  # Base de datos detalle_ventas
                contenido = """- Nombre de la BBDD: detalle_ventas
- Cantidad de columnas: 6 columnas
- Cantidad de observaciones (filas): 120 observaciones o registros
- Archivo con extensión xlsx

Variables:
1. id_venta: cuantitativo (int), discreto, estructurado, intervalo
2. id_producto: cuantitativo (int), discreto, estructurado, intervalo
3. nombre_producto: cualitativo (string), categórico, no estructurado, nominal
4. cantidad: cuantitativo (int), discreto, estructurado, razón
5. precio_unitario: cuantitativo (int), continuo, estructurado, razón
6. importe: cuantitativo (int), continuo, estructurado, razón"""
                self.mostrar_texto_paginado(contenido)

        elif seccion_principal == 4:  # Definición del problema y solución
            if subseccion == 1:  # Problema
                contenido = """Actualmente no contamos con una vista consolidada que muestre el aporte de
cada cliente a las ventas ni un desglose claro por categoría de productos,
medio de pago o zona geográfica. Esto dificulta la gestión comercial y estratégica.

Además, no se ha realizado un ejercicio de segmentación de clientes que permita
distinguir perfiles de consumo diferentes (por ejemplo, clientes frecuentes,
clientes de alto gasto, clientes inactivos)."""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 2:  # Solución
                contenido = """Desarrollar en Python un proceso que integre y analice las tablas clientes,
ventas, detalle_ventas y productos para:

1. Realizar un análisis exploratorio (EDA) de los datos disponibles
2. Limpiar los datos: Auditoría de categorías (categoria_std)
3. Integrar las tablas en una vista unificada
4. Generar reportes consolidados:
   - Ventas por cliente
   - Ventas por categoría
   - Ventas por medio de pago
   - Ventas por ciudad
   - Identificación de clientes sin compras"""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 3:  # Supuestos y reglas
                contenido = """- Se conserva siempre el dataset original
- Las categorías de productos pueden estar mal asignadas
- Los importes se validan como importe = cantidad * precio_unitario
- Nombres y categorías normalizados a snake_case"""
                self.mostrar_texto_paginado(contenido)
            
            elif subseccion == 4:  # KPIs principales
                contenido = """- Número total de clientes, clientes activos e inactivos
- Número total de ventas y ticket promedio
- Ingreso total y desglose por categoría de producto
- Distribución de ingresos por medio de pago
- Ingreso total por ciudad
- Top 5 clientes por monto total"""
                self.mostrar_texto_paginado(contenido)

if __name__ == "__main__":
    doc = DocumentacionInteractiva()
    doc.mostrar_menu_principal()