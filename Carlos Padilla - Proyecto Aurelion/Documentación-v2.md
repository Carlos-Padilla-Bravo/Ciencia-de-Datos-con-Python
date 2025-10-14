
# Proyecto Aurelion

En el marco del curso sobre Fundamentos de Inteligencia Artificial impartido por Guayer en conjunto con IBM se pretende desarrollar un programa en Python para dar cumplimiento con los requisitos del curso. Para tal fin se utilizarán distintas tablas de datos relacionadas con ventas de productos alimenticios y de limpieza. 

# Creación de carpeta en PC y descarga de archivos

Para desarrollar el Proyecto Aurelion se realizaron los siguientes pasos iniciales:

- Creación de carpeta en PC con el nombre de Carlos Padilla-Proyecto Aurelion
- Descarga de archivos con extensión xlsx desde Google Drive (4 archivos)
- Conexión carpeta "Carlos Padilla-Proyecto Aurelion" con Visual Studio Code (Add Folder to Workspace)
- Inspección inicial de cada archivo en VSC para conocer su contenido
- Creación de un archivo md para documentar el proyecto

# Descripción de las tablas xlsx

El proyecto tiene a disposición cuatro tablas (BBDD) con extensión xlsx. A continuación se describe el contenido de cada BBDD:

## Base de datos clientes

- Nombre de la BBDD: clientes
- Cantidad de columnas: 5 columnas
- Cantidad de observaciones (filas): 100 obervaciones o registros
- Archivo con extensión xlsx

 Esta BBDD contiene las siguientes variables dispuestas en columnas en el siguiente orden. Además se detalla el tipo de dato contendio en cada variable o columna:

1. **id_cliente:** cuantitativo (int), discreto, estructurado, intervalo
2. **nombre_cliente:** cualitativo (string), categórico, no estructurado, nominal
3. **email:** cualitativo (string), categórico, no estructurado, nominal
4. **ciudad:** cualitativo (string), categórico, no estructurado, nominal
5. **fecha_alta:** cuantitativo (formato fecha yy-mm-dd), discreto, estructurado, intervalo

**Notas adicionales:** No se observan valores faltantes en la BBDD de "clientes", es decir para cada observación o registro las columnas se encuentran completas. No se aprecia mayor necesidad de realizar algún tipo de limpieza específica en la BBDD. Se debería verificar si existen varlores duplicados (nombre_cliente, email). 

## Base de datos de productos

- Nombre de la BBDD: productos
- Cantidad de columnas: 4 columnas
- Cantidad de observaciones (filas): 100 obervaciones o registros
- Archivo con extensión xlsx

 Esta BBDD contiene las siguientes variables dispuestas en columnas en el siguiente orden. Además se detalla el tipo de dato contendio en cada variable o columna:

1. id_producto: cuantitativo (int), discreto, estructurado, intervalo
2. nombre_producto: cualitativo (string), categórico, no estructurado, nominal
3. categoria: cualitativo (string), categórico, no estructurado, nominal 
4. precio_unitario: cuantitativo (int), continuo, estructurado, razón

**Notas adicionales:** No se observan valores faltantes en la BBDD de "productos". La variable "categoria" presentanta dos categorias o segmentos (Alimentos y Limpieza). **Sin embargo, se observa que varios productos están mal clasificados en sus respectivas categorías.** Se debería verficiar si existen valores duplicados (nombre_producto).

## Base de datos de ventas

- Nombre de la BBDD: ventas
- Cantidad de columnas: 6 columnas
- Cantidad de observaciones (filas): 120 obervaciones o registros
- Archivo con extensión xlsx

 Esta BBDD contiene las siguientes variables dispuestas en columnas en el siguiente orden. Además se detalla el tipo de dato contendio en cada variable o columna:

 1. id_venta: cuantitativo (int), discreto, estructurado, intervalo
2. fecha: cuantitativo (formato fecha yy-mm-dd), discreto, estructurado, intervalo
3. id_cliente: cuantitativo (int), discreto, estructurado, intervalo
4. nombre_cliente: cualitativo (string), categórico, no estructurado, nominal
5. email: cualitativo (string), categórico, no estructurado, nominal
6. medio_pago: cualitativo (string), categórico, no estructurado, nominal

**Notas adicionales:** No se observan valores faltantes en la BBDD de "ventas". La variable "medio_pago" contiene las siguientes categorías: "tarjeta", "qr", "transferencia", "efectivo". Nótese que al contar con 120 registros, es un indicativo de que un cliente cuenta con más de una compra en el periodo, es decir, tiene más de un id_venta asociado.  

## Base de datos detalle_ventas

- Nombre de la BBDD: detalle_ventas
- Cantidad de columnas: 6 columnas
- Cantidad de observaciones (filas): 120 obervaciones o registros
- Archivo con extensión xlsx

 Esta BBDD contiene las siguientes variables dispuestas en columnas en el siguiente orden. Además se detalla el tipo de dato contendio en cada variable o columna:

1. id_venta: cuantitativo (int), discreto, estructurado, intervalo
2. id_producto: cuantitativo (int), discreto, estructurado, intervalo
3. nombre_producto: cualitativo (strig), categórico, no estructurado, nominal
4. cantidad: cuantitativo (int), discreto, estructurado, razón
5. precio_unitario: cuantitativo (int), continuo, estructurado, razón
6. importe: cuantitativo (int), continuo, estructurado, razón

**Notas adicionales:** No se observan valores faltantes en la BBDD de "detalle_ventas". Nótese que cada venta (id_venta) puede tener asociado más de un producto (id_producto).

# Requisitos de instalación y dependencias

Para ejecutar este proyecto se requieren los siguientes componentes:

## Python y bibliotecas
- Python versión 3.8 o superior
- pandas >= 2.0.0
- numpy >= 1.20.0
- openpyxl >= 3.0.0 (para lectura de archivos Excel)
- matplotlib >= 3.4.0 (para visualizaciones)
- seaborn >= 0.11.0 (para visualizaciones avanzadas)

## Instalación
```bash
pip install pandas==2.0.0 numpy==1.20.0 openpyxl==3.0.0 matplotlib==3.4.0 seaborn==0.11.0
```

# Especificaciones de formato de datos

## Formatos de fecha
- Todas las fechas deben estar en formato 'YYYY-MM-DD'
- Ejemplos válidos: '2025-10-13', '2024-01-01'
- Las fechas se almacenan como objetos datetime en pandas

## Formatos numéricos
- Precios: números decimales con 2 lugares decimales
- IDs: números enteros positivos
- Cantidades: números enteros positivos
- Importes: números decimales con 2 lugares decimales

## Validaciones de calidad de datos
Las siguientes validaciones se realizan durante el procesamiento:

1. Validación de fechas
   - Fecha_alta de cliente debe ser anterior a fecha de venta
   - No se permiten fechas futuras

2. Validación de precios e importes
   - Precios unitarios deben ser positivos y mayores a cero
   - Importe debe coincidir con cantidad * precio_unitario
   - Precios deben ser consistentes entre tablas de productos y detalle_ventas

3. Validación de integridad referencial
   - Todo id_cliente en ventas debe existir en tabla clientes
   - Todo id_producto en detalle_ventas debe existir en tabla productos
   - Todo id_venta en detalle_ventas debe existir en tabla ventas

4. Validación de duplicados
   - No se permiten emails duplicados en tabla clientes
   - No se permiten nombres de producto duplicados
   - Se verifica la unicidad de claves primarias (id_cliente, id_producto, id_venta)

# Definición del problema y solución

**Tema: Ventas de alimentos y productos de limpieza.**

## Problema

Actualmente no contamos con una vista consolidada que muestre el aporte de cada cliente a las ventas ni un desglose claro por categoría de productos, medio de pago o zona geográfica. Esto dificulta la gestión comercial y estratégica.

Además, no se ha realizado un ejercicio de segmentación de clientes que permita distinguir perfiles de consumo diferentes (por ejemplo, clientes frecuentes, clientes de alto gasto, clientes inactivos). La falta de segmentación impide diseñar acciones comerciales diferenciadas y dirigidas a cada grupo.

**Nota** La segmentación de clientes podría ser opcional. En esta versión no se incluye en el flujo de la solución. Requiere la aplicación de algún algoritrmo de machine learning (ej. clustering)

## Solución

Desarrollar en Python un proceso que integre y analice las tablas clientes, ventas, detalle_ventas y productos para:

1. Realizar un análisis exploratorio (EDA) de los datos disponibles.
2. Limpiar los datos: Auditoría de categorías (categoria_std).
3. Integrar las tablas en una vista unificada de clientes y transacciones.
4. Generar reportes consolidados:
    - Ventas por cliente
    - Ventas por categoría
    - Ventas por medio de pago
    - Ventas por ciudad
    - Identificación de clientes sin compras

## Supuestos y reglas

- Se conserva siempre el dataset original.
- Las categorías de productos pueden estar mal asignadas; por ello se define una columna categoria_std corregida mediante reglas o diccionario.
- Los importes se validan como importe = cantidad * precio_unitario. Si hay discrepancias, se recalculan y se registran en un log de calidad.
- Nombres y categorías normalizados a snake_case

## KPIs principales

- Número total de clientes, clientes activos e inactivos.
- Número total de ventas y ticket promedio.
- Ingreso total y desglose por categoría de producto.
- Distribución de ingresos por medio de pago.
- Ingreso total por ciudad.
- Top 5 clientes por monto total.

# Diagrama de flujo

[Inicio: Comienza el Proceso del Proyecto Aurelion]
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
[Proceso: Limpieza y Validación de Datos (Fase Ampliada)]
    |
    |--- 1. Validación de Formatos y Tipos de Datos
    |      |-> [Proceso: Convertir columnas de fecha a datetime, asegurar tipos numéricos (int, float)]
    |      '-> [Proceso: Registrar cualquier error de formato en log.txt]
    |
    |--- 2. Validación de Calidad de Datos (Tabla por Tabla)
    |      |-> Tabla 'productos':
    |      |   |-> [Proceso: Verificar duplicados en 'nombre_producto']
    |      |   '-> [Proceso: Verificar que 'precio_unitario' > 0]
    |      |-> Tabla 'clientes':
    |      |   '-> [Proceso: Verificar duplicados en 'email']
    |      |-> Tabla 'ventas':
    |      |   '-> [Proceso: Verificar que 'fecha' no sea futura]
    |      |-> Tabla 'detalle_ventas':
    |      |   |-> [Proceso: Calcular 'importe_calculado' = cantidad * precio_unitario]
    |      |   |-> <Decisión: ¿Hay discrepancias entre 'importe' e 'importe_calculado'?>
    |      |         |--- (SI) ---> [Proceso: Reemplazar 'importe' y registrar en log.txt]
    |      |         '--- (NO) ---> [Continuar]
    |
    |--- 3. Corrección de Categorías ('productos')
    |      '-> [Proceso: Crear columna 'categoria_std' corrigiendo categorías mal asignadas]
    |
    V
[Proceso: Integración de Datos (Merges) y Validación de Integridad]
    |-> [Proceso: Unir 'df_ventas' con 'df_detalle_ventas' -> df_ventas_completo]
    |      '-> <Decisión: ¿Hay 'id_venta' sin correspondencia (nulos)?>
    |            |--- (SI) ---> [Proceso: Registrar inconsistencia en log.txt y decidir estrategia (ej. eliminar fila)]
    |            '--- (NO) ---> [Continuar]
    |
    |-> [Proceso: Unir 'df_ventas_completo' con 'df_productos' (limpio)]
    |      '-> <Decisión: ¿Hay 'id_producto' sin correspondencia (nulos)?>
    |            |--- (SI) ---> [Proceso: Registrar inconsistencia en log.txt]
    |            '--- (NO) ---> [Continuar]
    |
    |-> [Proceso: Unir el resultado anterior con 'df_clientes' -> df_consolidado]
    |      |-> <Decisión: ¿Hay 'id_cliente' sin correspondencia (nulos)?>
    |      |     |--- (SI) ---> [Proceso: Registrar inconsistencia en log.txt]
    |      |     '--- (NO) ---> [Continuar]
    |      '-> [Proceso: Validar que 'fecha_alta' < 'fecha' de venta para cada transacción]
    |
    V
[Proceso: Cálculo de KPIs y Generación de Reportes]
    |
    |--- [Cálculo: KPIs de clientes (total, activos, inactivos)]
    |--- [Cálculo: KPIs de ventas (total, ticket promedio, ingreso total)]
    |--- [Cálculo: Desgloses por 'categoria_std', 'medio_pago', 'ciudad']
    |--- [Cálculo: Top 5 clientes por monto total]
    |
    V
[Salida: Presentación de Resultados]
    |-> [Salida: Imprimir KPIs principales en la consola]
    |-> [Salida: Guardar reportes en archivos CSV o Excel]
    |-> [Salida: Guardar df_consolidado en un archivo CSV]
    |
    V
[Fin: Proceso Completado]


# Pseudocódigo


INICIO_PROGRAMA

// -----------------------------------------------------
// FASE 1: CARGA Y PREPARACIÓN DE DATOS
// -----------------------------------------------------
// Cargar los datos desde los archivos fuente.
df_clientes = CARGAR_EXCEL("clientes.xlsx")
df_productos = CARGAR_EXCEL("productos.xlsx")
df_ventas = CARGAR_EXCEL("ventas.xlsx")
df_detalle_ventas = CARGAR_EXCEL("detalle_ventas.xlsx")

// Crear copias de respaldo para mantener los datos originales intactos.
df_clientes_orig = COPIAR(df_clientes)
df_productos_orig = COPIAR(df_productos)
df_ventas_orig = COPIAR(df_ventas)
df_detalle_ventas_orig = COPIAR(df_detalle_ventas)

// -----------------------------------------------------
// FASE 2: ANÁLISIS EXPLORATORIO DE DATOS (EDA)
// -----------------------------------------------------
IMPRIMIR("--- Iniciando Análisis Exploratorio de Datos (EDA) ---")

// Realizar una inspección básica para cada tabla cargada.
LISTA_DATAFRAMES = [df_clientes, df_productos, df_ventas, df_detalle_ventas]
NOMBRES_DATAFRAMES = ["Clientes", "Productos", "Ventas", "Detalle_Ventas"]

FOR i FROM 0 TO LONGITUD(LISTA_DATAFRAMES) - 1:
    df_actual = LISTA_DATAFRAMES[i]
    nombre_actual = NOMBRES_DATAFRAMES[i]

    IMPRIMIR(f"\n--- Resumen de la tabla: {nombre_actual} ---")
    // 1. Mostrar las primeras filas para entender la estructura.
    IMPRIMIR("Primeras 5 filas:")
    MOSTRAR_HEAD(df_actual, 5)

    // 2. Mostrar información general: número de filas, columnas, tipos de datos y nulos.
    IMPRIMIR("\nInformación de columnas y tipos de datos:")
    MOSTRAR_INFO(df_actual)

    // 3. Mostrar estadísticas descriptivas para las columnas numéricas.
    IMPRIMIR("\nEstadísticas descriptivas (columnas numéricas):")
    MOSTRAR_DESCRIBE(df_actual)
FIN FOR

// -----------------------------------------------------
// FASE 3: LIMPIEZA Y VALIDACIÓN (VERSIÓN EXTENDIDA)
// -----------------------------------------------------
IMPRIMIR("--- Iniciando Limpieza y Validación de Datos ---")

// 3.1 Validación de formatos y tipos de datos
// (Se asume que las funciones de carga intentan convertir tipos, aquí se verifica)
df_ventas['fecha'] = CONVERTIR_A_FECHA(df_ventas['fecha'], errores='registrar')
df_clientes['fecha_alta'] = CONVERTIR_A_FECHA(df_clientes['fecha_alta'], errores='registrar')
// ... (verificar tipos numéricos para precios, cantidades, etc. y registrar errores)

// 3.2 Verificación de calidad de datos a nivel de tabla
// 3.2.1 Tabla Clientes
IF HAY_DUPLICADOS(df_clientes, 'email') ENTONCES
    ESCRIBIR_LOG("Advertencia: Se encontraron emails duplicados en la tabla de clientes.")
FIN IF

// 3.2.2 Tabla Productos
IF HAY_DUPLICADOS(df_productos, 'nombre_producto') ENTONCES
    ESCRIBIR_LOG("Advertencia: Se encontraron nombres de producto duplicados.")
FIN IF
IF CUALQUIER(df_productos['precio_unitario'] <= 0) ENTONCES
    ESCRIBIR_LOG("Error de Calidad: Existen productos con precio unitario menor o igual a cero.")
FIN IF

// 3.2.3 Tabla Ventas
IF CUALQUIER(df_ventas['fecha'] > FECHA_ACTUAL()) ENTONCES
    ESCRIBIR_LOG("Error de Calidad: Existen ventas con fechas futuras.")
FIN IF

// 3.2.4 Corrección de categorías en 'df_productos'
df_productos['categoria_std'] = df_productos['categoria'] // Columna base

diccionario_correccion = { "leche descremada": "alimentos", "jabon en polvo": "limpieza", "arroz integral": "alimentos" }

FOR CADA fila IN df_productos:
    nombre_prod = fila['nombre_producto']
    categoria_actual = fila['categoria_std']
    categoria_corregida = categoria_actual // Valor por defecto

    // Lógica IF/ELSE IF para reglas generales
    IF nombre_prod IN diccionario_correccion ENTONCES
        categoria_corregida = diccionario_correccion[nombre_prod]
    ELIF "detergente" IN nombre_prod OR "lavandina" IN nombre_prod ENTONCES
        categoria_corregida = "limpieza"
    ELIF "queso" IN nombre_prod OR "pan" IN nombre_prod ENTONCES
        categoria_corregida = "alimentos"
    FIN IF

    // Aplicar el cambio si es necesario.
    IF categoria_corregida != categoria_actual ENTONCES
        fila['categoria_std'] = categoria_corregida
        ESCRIBIR_LOG(f"Categoría corregida para '{nombre_prod}': de '{categoria_actual}' a '{categoria_corregida}'")
    FIN IF
FIN FOR

// 3.2.5 Validación y corrección de importes en 'df_detalle_ventas'
df_detalle_ventas['importe_calculado'] = df_detalle_ventas['cantidad'] * df_detalle_ventas['precio_unitario']

IF CUALQUIER(df_detalle_ventas['importe'] != df_detalle_ventas['importe_calculado']) ENTONCES
    ESCRIBIR_LOG("Advertencia: Inconsistencias encontradas en la columna 'importe'. Se recalcularán los valores.")
    // Corregir la columna original con los valores calculados.
    df_detalle_ventas['importe'] = df_detalle_ventas['importe_calculado']
FIN IF

// -----------------------------------------------------
// FASE 4: INTEGRACIÓN DE DATOS Y VALIDACIÓN DE INTEGRIDAD
// -----------------------------------------------------
// 4.1 Fusión de ventas y su detalle
df_ventas_detalle = FUSIONAR(df_ventas, df_detalle_ventas, en='id_venta', tipo='left')
// Un id_venta sin detalle es posible, pero un detalle sin id_venta generaría nulos en las columnas de 'df_ventas'
// La validación de integridad se hará post-fusiones para ser más eficientes.

// 4.2 Fusión con productos
df_temp = FUSIONAR(df_ventas_detalle, df_productos, en='id_producto', tipo='left')

// 4.3 Fusión con clientes para obtener el consolidado
df_consolidado = FUSIONAR(df_temp, df_clientes, en='id_cliente', tipo='left')

// 4.4 Validaciones de Integridad y Lógica de Negocio (Post-Integración)
IF HAY_NULOS(df_consolidado, 'nombre_producto') ENTONCES
    ESCRIBIR_LOG("Error de Integridad: Existen productos en 'detalle_ventas' que no están en la tabla 'productos'.")
FIN IF
IF HAY_NULOS(df_consolidado, 'nombre_cliente') ENTONCES
    ESCRIBIR_LOG("Error de Integridad: Existen clientes en 'ventas' que no están en la tabla 'clientes'.")
FIN IF
IF CUALQUIER(df_consolidado['fecha_alta'] > df_consolidado['fecha']) ENTONCES
    ESCRIBIR_LOG("Error de Lógica: Existen ventas registradas antes de la fecha de alta del cliente.")
FIN IF

// -----------------------------------------------------
// FASE 5: CÁLCULO DE KPIS Y AGREGACIONES
// -----------------------------------------------------
// --- Métricas de Clientes ---
total_clientes = CONTAR_UNICOS(df_clientes['id_cliente'])
ids_clientes_activos = OBTENER_UNICOS(df_consolidado['id_cliente'])
clientes_activos_count = LONGITUD(ids_clientes_activos)
clientes_inactivos_count = total_clientes - clientes_activos_count
df_clientes_sin_compras = FILTRAR(df_clientes, donde 'id_cliente' NO ESTA EN ids_clientes_activos)

// --- Métricas de Ventas ---
total_ventas = CONTAR_UNICOS(df_consolidado['id_venta'])
ingreso_total = SUMA(df_consolidado['importe'])

// Cálculo de ticket promedio con protección contra división por cero.
IF total_ventas > 0 ENTONCES
    ticket_promedio = ingreso_total / total_ventas
ELSE
    ticket_promedio = 0
FIN IF

// --- Generación de Reportes Agrupados ---
ventas_por_cliente = AGRUPAR_POR(df_consolidado, 'nombre_cliente').SUMAR('importe').ORDENAR_DESC()
ventas_por_categoria = AGRUPAR_POR(df_consolidado, 'categoria_std').SUMAR('importe')
ventas_por_medio_pago = AGRUPAR_POR(df_consolidado, 'medio_pago').SUMAR('importe')
ventas_por_ciudad = AGRUPAR_POR(df_consolidado, 'ciudad').SUMAR('importe')
top_5_clientes = ventas_por_cliente.TOMAR_LOS_PRIMEROS(5)

// -----------------------------------------------------
// FASE 6: SALIDA Y EXPORTACIÓN DE RESULTADOS
// -----------------------------------------------------
// Imprimir un resumen ejecutivo en la consola.
IMPRIMIR("--- KPIs Principales del Proyecto Aurelion ---")
IMPRIMIR(f"Número total de clientes: {total_clientes}")
IMPRIMIR(f"Clientes activos (con compras): {clientes_activos_count}")
IMPRIMIR(f"Clientes inactivos (sin compras): {clientes_inactivos_count}")
IMPRIMIR("----------------------------------------------")
IMPRIMIR(f"Número total de ventas: {total_ventas}")
IMPRIMIR(f"Ingreso Total: ${ingreso_total:.2f}")
IMPRIMIR(f"Ticket Promedio por Venta: ${ticket_promedio:.2f}")
IMPRIMIR("\n--- Top 5 Clientes por Ingreso ---")
IMPRIMIR(top_5_clientes)
IMPRIMIR("\n--- Ingresos por Categoría de Producto ---")
IMPRIMIR(ventas_por_categoria)

// Guardar los reportes principales y la tabla consolidada en archivos CSV.
GUARDAR_A_CSV(df_consolidado, "reporte_consolidado_final.csv")
GUARDAR_A_CSV(ventas_por_ciudad, "reporte_ventas_por_ciudad.csv")
GUARDAR_A_CSV(ventas_por_categoria, "reporte_ventas_por_categoria.csv")
GUARDAR_A_CSV(df_clientes_sin_compras, "reporte_clientes_sin_compras.csv")

IMPRIMIR("\nProceso finalizado. Los reportes han sido generados exitosamente.")

FIN_PROGRAMA

