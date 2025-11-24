
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
- Cantidad de observaciones (filas): 343 obervaciones o registros
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
    |--- [Cálculo: Top 10 clientes por monto total]
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
metricas_cliente = AGRUPAR_POR(df_consolidado, 'nombre_cliente').SUMAR('importe').ORDENAR_DESC()
metricas_producto = AGRUPAR_POR(df_consolidado, 'categoria_std').SUMAR('importe')
metricas_pago = AGRUPAR_POR(df_consolidado, 'medio_pago').SUMAR('importe')
metricas_ciudad = AGRUPAR_POR(df_consolidado, 'ciudad').SUMAR('importe')


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
IMPRIMIR(metricas_producto)

// Guardar los reportes principales y la tabla consolidada en archivos CSV.
GUARDAR_A_CSV(df_consolidado, "reporte_consolidado_final.csv")
GUARDAR_A_CSV(df_metricas_cliente, "metricas_cliente.csv")
GUARDAR_A_CSV(df_metricas_producto, "metricas_producto.csv")
GUARDAR_A_CSV(df_metricas_pago, "metricas_pago.csv")
GUARDAR_A_CSV(df_metricas_ciudad, "metricas_ciudad.csv")

IMPRIMIR("\nProceso finalizado. Los reportes han sido generados exitosamente.")

FIN_PROGRAMA

# Análisis Exploratorio de Datos y Proceso de Limpieza (EDA)

A continuación, se detalla el proceso de análisis exploratorio (EDA) y limpieza realizado sobre cada uno de los dataframes del proyecto.

## Análisis del Dataframe `df_clientes`

Para el dataframe de clientes, el análisis se centró en garantizar la calidad e integridad de los datos.

- **Estructura y Calidad:** Se confirmó que el dataframe contiene 100 filas y 5 columnas, sin valores nulos. Los tipos de datos eran correctos para cada columna (`id_cliente` como numérico, `fecha_alta` como fecha, etc.).
- **Análisis de Duplicados:**
    - Se verificó que todos los `id_cliente` y `email` son únicos, lo cual es crucial para la integridad de los datos.
    - Se encontraron 5 nombres de clientes (`nombre_cliente`) duplicados. Sin embargo, al revisar los registros completos, se observó que correspondían a personas distintas (homónimos) con diferentes `id_cliente`, `email` y, en algunos casos, `ciudad`. Por lo tanto, se decidió no eliminarlos.
- **Análisis de Variables Categóricas:** Se identificaron 6 ciudades únicas, siendo Córdoba, Río Cuarto y Alta Gracia las que concentran la mayor cantidad de clientes.

![Distribución de Clientes por Ciudad (df_clientes)](Figuras/Distribución%20de%20Clientes%20por%20Ciudad%20(df_clientes).png)

## Análisis del Dataframe `df_productos`

El análisis de este dataframe fue fundamental, ya que se detectaron inconsistencias en la clasificación de productos.

- **Estructura y Calidad:** El dataframe consta de 100 productos con 4 columnas, sin valores nulos ni filas duplicadas. Los `id_producto` y `nombre_producto` son únicos.
- **Análisis de Precios:** El `precio_unitario` de los productos varía entre $272 y $4,982, con una distribución que muestra dos picos de frecuencia (multimodal), sugiriendo la existencia de dos grupos de productos según su precio.

![Distribución de Precio Unitario (df_productos)](Figuras/Distribución%20de%20Precio%20Unitario%20(df_productos).png)

![Box Plot de Precio Unitario (df_productos)](Figuras/Box%20Plot%20de%20Precio%20Unitario%20(df_productos).png)

- **Reclasificación de Productos:**
    1. **Detección de Inconsistencias:** El análisis inicial reveló que la columna `categoria` presentaba productos de "Limpieza" clasificados erróneamente como "Alimentos" y viceversa. Por ejemplo, productos como "Detergente Líquido" o "Lavandina" no estaban correctamente asignados.
    2. **Corrección Inicial:** Se identificó un conjunto de 17 productos que claramente pertenecían a la categoría "Limpieza". A través de la creación de un set (Limpieza) se creó una nueva columna `categoria_corregida` y un nuevo dataframe (`df_productos_nuevo`) para asignar correctamente estos productos a "Limpieza" y el resto a "Alimentos". Además se procedió a eliminar en este dataframe la columna original `categoria`.
    3. **Creación de Nuevas Categorías:** Para un análisis más granular, se crearon subcategorías dentro de "Alimentos" a partir de tres diccionarios. Se definieron las categorías `Bebidas_Frias`, `Bebidas_Calientes` y `Bebidas_Alcoholicas` a partir de los nombres de los productos. Los productos que no encajaban en estas nuevas categorías permanecieron como "Alimentos".
    4. **Resultado Final:** Este proceso resultó en un dataframe de productos reclasificado (`df_productos_reclasificado`) con 5 categorías (`Alimentos`, `Limpieza`, `Bebidas_Frias`, `Bebidas_Calientes`, `Bebidas_Alcoholicas`), lo que permitió un análisis de KPIs mucho más preciso.

![Distribución Productos por Categoría (df_productos_reclasificado)](Figuras/Distribución%20Productos%20por%20Categoría%20(df_productos_reclasificado).png) 

- **Análisis Estadístico por Categoría:** Se realizó un análisis estadístico descriptivo del `precio_unitario` agrupado por las nuevas categorías, obteniéndose los siguientes resultados:

|Categoría	         |Número de Productos |Media   |Desv. Estándar	|Mínimo	|Primer Cuartil	|Mediana	|Tercer Cuartil	|Máximo
|--------------------|--------------------|--------|----------------|-------|---------------|-----------|---------------|------
|Alimentos           |57.0                |2590.6  |1388.4          |272.0  |1571.0         |2502.0     |3848.0         |4982.0
|Bebidas_Alcoholicas |11.0                |2569.6  |1371.5          |508.0  |1547.0         |2684.0     |3540.0         |4719.0
|Bebidas_Calientes   |5.0                 |2753.4  |1672.9          |570.0  |2053.0         |2383.0     |3878.0         |4883.0
|Bebidas_Frias       |10.0                |3669.7  |1211.3          |1856.0 |2577.5         |4130.0     |4637.3         |4973.0
|Limpieza            |17.0                |2674.2  |1312.5          |872.0  |1592.0         |2512.0     |2902.0         |4920.0

![Box Plot del Precio Unitario por Categoría de Producto (df_productos_reclasificado)](Figuras/Box%20Plot%20del%20Precio%20Unitario%20por%20Categoría%20de%20Producto%20(df_productos_reclasificado).png)

## Análisis del Dataframe `df_detalle_ventas`

Este dataframe fue clave para validar la consistencia de las transacciones.

- **Estructura y Calidad:** Contiene 343 registros y 6 columnas, sin valores nulos. Además, se verificó la ausencia de filas duplicadas.
- **Consistencia de Productos:** Se identificó solo 95 id_productos únicos en `df_detalle_ventas`, lo que indica que NO todos los productos del catálogo fueron vendidos durante el período analizado.

Productos en catálogo que no están en detalle_ventas:

|id_producto      |nombre_producto    |precio_unitario |nueva_categoria  
|-----------------|-------------------|----------------|-----------------
|60               |Chupetín           |4647            |Alimentos   
|69               |Sidra 750ml        |744             |Bebidas_Alcoholicas   
|75               |Licor de Café 700ml|3204            |Bebidas_Alcoholicas   
|96               |Suavizante 1L      |4920            |Limpieza   
|99               |Esponjas x3        |2430            |Limpieza 

- **Consistencia de precios unitarios:** Se verificó que los `precio_unitario` en este dataframe coincidieran con los precios unitarios en el dataframe de productos_reclasificado. No se encontraron discrepancias.
- **Validación de Importes:** Se realizó una validación cruzada para asegurar que la columna `importe` fuera consistente con el cálculo de `cantidad * precio_unitario`. Se creó una columna `importe_calculado` para verificar esto. **No se encontraron discrepancias**, confirmando que los importes registrados eran correctos. Posteriormente se eliminó (drop) la columna `importe_calculado` del dataframe, manteniendo solo la columna `importe` original.
- **Análisis de Outliers en Importe:** Mediante un box plot, se detectaron valores atípicos (`outliers`) en la columna `importe`. Un análisis más profundo reveló que estos valores correspondían a compras de gran volumen o de productos con alto precio unitario, y no a errores de datos. Por lo tanto, se decidió conservarlos, ya que representan patrones de compra válidos y valiosos para el negocio.

![Distribución Importe en Detalle Ventas (df_detalle_ventas)](Figuras/Distribución%20Importe%20en%20Detalle%20Ventas%20(df_detalle_ventas).png)
![Box Plot de Importe (df_detalle_ventas)](Figuras/Box%20Plot%20de%20Importe%20(df_detalle_ventas).png)

- **Análisis de Cantidades Vendidas:** La cantidad de unidades vendidas por producto varió entre 1 y 5, con una media de 3 y moda 2.

![Distribución de Cantidad Por Venta en Detalle de Ventas (df_detalle_ventas)](Figuras/Distribución%20de%20Cantidad%20Por%20Venta%20en%20Detalle%20de%20Ventas%20(df_detalle_ventas).png)
![Box Plot de Cantidad Vendida (df_detalle_ventas)](Figuras/Box%20Plot%20de%20Cantidad%20Vendida%20(df_detalle_ventas).png)

## Análisis del Dataframe `df_ventas`

Finalmente, el dataframe de ventas se analizó para entender el comportamiento general de las transacciones.

- **Estructura y Calidad:** Compuesto por 120 filas y 6 columnas, sin valores nulos. Se constató también la ausencia de filas duplicadas en el dataframe.
- **Análisis de Duplicados:** Se confirmó que todos los `id_venta` son únicos, asegurando la integridad de las transacciones.
- **Cambio nombre columna fecha:** Se renombró la columna `fecha` a `fecha_venta` para mayor claridad.
- **Verificando id_cliente en rango válido:** Se validó que todos los `id_cliente` en este dataframe existieran en el dataframe `df_clientes` y estubieran contendios en el rango 1 a 100. No se encontraron inconsistencias.
- **Análisis de Clientes:** Se identificaron 67 clientes únicos que realizaron compras, lo que indica que 33 clientes del dataframe `df_clientes` no realizaron ninguna compra durante el período analizado.
- **Verificando que los pares nombre_cliente + email en df_ventas existen en df_clientes:** Se validó que todos los pares `nombre_cliente` + `email` en este dataframe coincidieran con los registros en el dataframe `df_clientes`. No se encontraron discrepancias.
- **Verificando que fecha_venta en df_ventas sea posterior a fecha_alta en df_clientes:** Se verificó que todas las fechas de venta fueran posteriores a las fechas de alta de los clientes correspondientes. No se encontraron violaciones a esta regla.
- **Distribución de número de ventas por mes:** Se observó que la mayoría de las ventas se concentraron en enero mientras que abril tuvo la menor cantidad de transacciones.

![Distribución de Ventas por Mes (df_ventas)](Figuras/Distribución%20de%20Ventas%20por%20Mes%20(df_ventas).png)

- **Distribución de transacciones por medio de pago:** Se analizó la distribución de las ventas según el medio de pago utilizado, encontrando que el efectivo fue el método más popular, seguido por QR.

![Distribución de Ventas por Medio de Pago (df_ventas)](Figuras/Distribución%20de%20Ventas%20por%20Medio%20de%20Pago%20(df_ventas).png)

## Validación de Integridad referencial entre dataframes

Se realizaron validaciones de integridad referencial entre los dataframes para asegurar que las claves foráneas coincidieran con las claves primarias correspondientes:

- **Validación entre `df_ventas` y `df_clientes`:** Se confirmó que todos los `id_cliente` en `df_ventas` existen en `df_clientes`. No se encontraron inconsistencias.
- **Validación entre `df_detalle_ventas` y `df_productos_reclasificado`:** Se verificó que todos los `id_producto` en `df_detalle_ventas` existen en `df_productos_reclasificado`. No se encontraron discrepancias.
- **Validación entre `df_detalle_ventas` y `df_ventas`:** Se aseguró que todos los `id_venta` en `df_detalle_ventas` existen en `df_ventas`. No se detectaron inconsistencias.

## Consolidación de datos en un único DataFrame

Tras completar el análisis exploratorio y la limpieza de los datos, se procedió a consolidar la información en un único dataframe (`consolidado`) mediante una serie de fusiones (merges) entre los dataframes limpios:

1. **Fusión de `df_ventas` y `df_detalle_ventas`:** Se realizó una fusión izquierda (`left join`) utilizando la columna `id_venta` como clave. Esto permitió combinar la información de las ventas con los detalles de cada transacción.
2. **Fusión con `df_productos_reclasificado`:** El resultado anterior se fusionó nuevamente con el dataframe de productos reclasificado, utilizando `id_producto` como clave. Esto añadió la información de los productos vendidos, incluyendo las categorías corregidas.
3. **Fusión con `df_clientes`:** Finalmente, se fusionó el dataframe resultante con el dataframe de clientes, utilizando `id_cliente` como clave. Esto incorporó los datos demográficos y de contacto de los clientes a cada transacción.

## Eliminación de columnas repetidas y renombrado de columnas

- **Eliminación de redundancias:** Se eliminaron las columnas repetidas (nombre_cliente_y', 'email_y', 'nombre_producto_y', 'precio_unitario_y) generadas durante las fusiones y se renombraron algunas columnas para mejorar la claridad y consistencia del dataframe final.
- **Breve inspección del df_consolidado:** aplicando el método info y shape se inspeccionó el contendio del df_consolidado para verificar la consistencia y contendio del dataframe. No se hayaron anomalías en el dataframe constituido en 343 filas y 15 columnas.

## Guardado del DataFrame consolidado

El dataframe consolidado final (`consolidado`) se guardó en un archivo XLSX `consolidado.xlsx` y en un archivo CSV llamado `consolidado.csv` para su posterior análisis y generación de reportes.

FIN_EDA

# Análisis de Reportes y Métricas Clave

Esta sección resume los principales KPIs y métricas obtenidas a partir de distintos reportes (dataframes) generados desde `consolidado` en el archivo `KPI_Reportes.ipynb`. El archivo originalse importo como `df_consolidado`. Se presentan los resultados clave por cliente, producto, ciudad y medio de pago, así como la segmentación de clientes y los principales insights extraídos a partir del análisis desagregado.

## 1. Métricas Generales

- **Total de clientes registrados:** 100
- **Clientes activos (con compras):** 67
- **Clientes inactivos (sin compras):** 33
- **Porcentaje de clientes activos:** 67%
- **Total de ventas (transacciones únicas):** 120
- **Ingreso total:** $2,651,417.00
- **Ticket promedio por venta:** $22,095.14

## 2. Métricas por Cliente

A partitr del dataframe `df_consolidado` se construyo el dataframe `metricas_cliente` conteniendo las siguientes columnas: email, ciudad, total_compras, importe_total, ticket_promedio, desviacion_estandar, productos_diferentes, categorias_diferentes, primera_compra, ultima_compra.

El dataframe `metricas_cliente` se guardo como archivo CSV llamado `metricas_cliente.csv`.

**Top 10 clientes por importe total:**

|--------------------------------------------------------|
| Cliente             | Ciudad       | Importe Total ($) |
|---------------------|--------------|-------------------|
| Agustina Flores     | Cordoba      | 132,158           |
| Bruno Diaz          | Rio Cuarto   | 90,701            |
| Diego Diaz          | Rio Cuarto   | 90,522            |
| Karina Castro       | Rio Cuarto   | 81,830            |
| María López         | Carlos Paz   | 72,448            |
| Olivia Gomez        | Rio Cuarto   | 71,321            |
| Guadalupe Martínez  | Rio Cuarto   | 67,959            |
| Pablo Sánchez       | Cordoba      | 67,575            |
| Camila Rodríguez    | Cordoba      | 65,001            |
| Santiago Díaz       | Alta Greacia | 64,786            |
|--------------------------------------------------------|

![Top Ten Clientes por Importe Total](Figuras/Top%20Ten%20Clientes%20por%20Importe%20Total.png)

**Distribución del ticket promedio por cliente:** La distribución del ticket promedio muestra una media de $23,505 y una mediana de $20,920, con algunos clientes de alto valor que elevan el promedio general.

![Distribución del Ticket Promedio](Figuras/Distribución%20del%20Ticket%20Promedio.png)

**Distribución de clientes por ciudad y ticket promedio:** Se observa que las ciudades con mayor número de clientes activos son Río Cuarto,  Alta Gracia y Cordoba. Sin embargo el ticket promedio en estas ciudades es inferior al de otras ciudades como Villa María, Carlos Paz y Mendiolaza, que presentan un ticket promedio más alto a pesar de tener menos clientes. Esto indica que el volumen de clientes no siempre se traduce en mayores ingresos por cliente.

![Distribución de Clientes por Ciudad y Ticket Promedio](Figuras/Distribución%20de%20Clientes%20por%20Ciudad%20y%20Ticket%20Promedio.png)

**Distribución del Ticket Promedio por Ciudad:** Se destaca que Villa María y Carlos Paz tienen el ticket promedio más alto, lo que sugiere un mayor poder adquisitivo en estas localidades. Se observa la presencia de outliers en ciudades como Carlos Paz y Alta Gracia, indicando que algunos clientes realizan compras significativamente mayores al promedio en estas ciudades.

![Distribución del Ticket Promedio por Ciudad](Figuras/Distribución%20del%20Ticket%20Promedio%20por%20Ciudad.png)

**Distribución de la frecuencia de compras por cliente:**  media 49.4 y mediana 37.3, con una alta variabilidad, lo que indica que algunos clientes compran con mucha más frecuencia que otros.

La frecuencia de compra se interpreta como el número promedio de días que transcurren entre compras consecutivas de un mismo cliente.

- Cálculo: Se toma el total de días entre la primera y la última compra del cliente y se divide por el número de intervalos entre esas compras (total_compras - 1).

- Interpretación:
Un valor bajo (ej. 5 días) significa que el cliente compra con mucha frecuencia, en promedio cada 5 días.
Un valor alto (ej. 60 días) indica que el cliente compra con menos frecuencia, en promedio cada 60 días.

![Distribución de la Frecuencia de Compra](Figuras/Distribución%20de%20la%20Frecuencia%20de%20Compra.png)

**Correlaciones entre métricas de clientes:** Se identificaron correlaciones positivas significativas entre:

('total_compras', 'importe_total'),          # Correlación ~0.65
('total_compras', 'productos_diferentes'),   # Correlación ~0.72
('productos_diferentes', 'importe_total'),   # Correlación ~0.83
('productos_diferentes', 'categorias_diferentes') # Correlación ~0.68

Esto sugiere que los clientes que realizan una mayor cantidad de compras en el periodo analizado, tienden a gastar más y a diversificar sus compras. Además, aquellos que adquieren una mayor variedad de productos también tienden a gastar más en total. Por su parte, la cantidad de categorías diferentes compradas está relacionada positivamente con la diversidad de productos adquiridos.

![Mapa Calor Métricas Clientes](Figuras/Mapa%20Calor%20Métricas%20Clientes.png)
![Scatter Plots Métricas Clientes](Figuras/Scatter%20Plots%20Métricas%20Clientes.png)


## 3. Métricas por Producto y Categoría

A partitr del dataframe `df_consolidado` se construyo el dataframe `metricas_producto` conteniendo las siguientes columnas: n_ventas (ventas por producto),unidades_vendidas, importe_total, importe_promedio, importe_std (desviación estándar), precio_unitario, n_clientes_unicos.

El dataframe `metricas_producto` se guardo como archivo CSV llamado `metricas_producto.csv`.

**Principales categorías (por importe total y unidades vendidas):**

|---------|-------------------------------------------------------------------|
| Categoría             | Importe Total ($) | % del Total | Unidades Vendidas |
|---------------------- |------------------ |-------------|-------------------|
| Alimentos             | 1,374,841         | 51.9%       | 581               |
| Limpieza              | 436,736           | 16.5%       | 170               |
| Bebidas Frías         | 382,959           | 14.5%       | 106               |
| Bebidas Alcohólicas   | 282,375           | 10.7%       | 100               |
| Bebidas Calientes     | 174,506           | 6.6%        | 59                |
|-----------------------------------------------------------------------------|

La categoría Alimentos lidera en ingresos y unidades, seguida por Limpieza y Bebidas.

![Rendimiento por Categoría de Producto](Figuras/Rendimiento%20por%20Categoría%20de%20Producto.png)
![Distribución Porcentual Unidades e Importe por Categoría](Figuras/Distribución%20Porcentual%20Unidades%20e%20Importe%20por%20Categoría.png)

**Evolución mensual de unidades vendidas e importe total por categoría de producto:** Se observa una tendencia estacional en la categoría Alimentos, tanto en unidades como importe, con un decenso marcado en abril y posteriormewnte un repunte,  mientras que el resto de categorías se comporta de forma estable a través de los meses. Bebidas Frías presenta un pico en el mes de mayo en términos de importe total.

![Evolución Temporal Unidades-Importe por Categoría Producto](Figuras/Evolución%20Temporal%20Unidades-Importe%20por%20Categoría%20Producto.png)

**Distribución de precios unitarios por categoría de producto:** Se observa que la categoría Bebidas Frías presenta un precio unitario promedio más alto respecto al resto de las categorías.  En general se observa un alata dispersión de precios dentro de cada categoría, con presencia de outliers en la categoría Limpieza, indicando que existen productos con precios significativamente mayores al promedio de su categoría.

![Distribución de Precios Unitarios por Categoría](Figuras/Distribución%20de%20Precios%20Unitarios%20por%20Categoría.png)

**Top 10 productos más vendidos por importe total, descendente:**

Se oberva que los productos más vendidos en términos de importe total pertenecen principalmente a las categorías de Alimentos y Bebidas, con excepción del Desodorante aerosol que pertenece a la categoría Limpieza.

|--------------------------------------------------------------------|
| Producto                  | Categoría          | Importe Total ($) |
|------------------------   |--------------------|-------------------|
| Desodorante aerosol       | Limpieza           | 98,800            |
| Queso Rallado 150g        | Alimentos          | 89,544            |
| Piza Congelada Muzzarella | Alimentos          | 85,720            |
| Ron 700ml                 | Bebidas Alcohólicas| 81,396            |
| Yerba Mate Suave 1kg      | Bebidas Calientes  | 77,560            |
| Energética Nitro 500ml    | Bebidas Frías      | 71,706            |
| Chicle de menta           | Alimentos          | 68,628            |
| Cramelos Masticables      | Alimentos          | 66,528            |
| Vino Blanco 750mlñ        | Bebidas Alcohólicas| 59,048            |
| Hamburguesas Congeladas x4| Alimentos          | 58,080            |
|----------------------------------------------------------------------------------------|

![Top Ten Productos Unidades-Importe](Figuras/Top%20Ten%20Productos%20Unidades-Importe.png)

## 4. Métricas por Medio de Pago

A partitr del dataframe `df_consolidado` se construyo el dataframe `metricas_pago` conteniendo las siguientes columnas: n_transacciones (número transacciones),importe_total, ticket_promedio, desviacion_estandar, n_clientes_unicos, n_productos_vendidos', primera_venta, ultima_venta

El dataframe `metricas_producto` se guardo como archivo CSV llamado `metricas_pago.csv`.

**Distribución de transacciones e ingresos por medio de pago (por importe total, descendente):**

|------------------------------------------------------------------------------------------|
| Medio de Pago | N° Transacciones | % Transacciones | Importe Total ($) | % Importe Total |
|---------------|------------------|-----------------|-------------------|-----------------|
| Efectivo      | 37               | 30,8%           | 934,819           | 35,3%           |
| QR            | 30               | 25.0%           | 714,280           | 26,9%           |
| Transferencia | 27               | 22,5%           | 542,219           | 20.5%           |
| Tarjeta       | 26               | 21,7%           | 460,099           | 17,4%           |
|------------------------------------------------------------------------------------------|

Predomina el uso de efectivo, pero con una impotante particpación de medios digitales, principalmente QR.

![Transacciones e Importe por Medio de Pago](Figuras/Transacciones%20e%20Importe%20por%20Medio%20de%20Pago.png)
![Distribución Porcentual Transacciones e Importe por Medio de Pago](Figuras/Distribución%20Porcentual%20Transacciones%20e%20Importe%20por%20Medio%20de%20Pago.png)

**Distribución del ticket por medio de pago:** El ticket es más alto en QR y efectivo, mientras que el tarjeta y transfrencia presentan tickets más bajos. Hay presencia de outliers en tarjeta y transferencia que reflejan clientes con compras significativamente mayores al promedio de cada medio de pago.

![Distribución Ticket por Medio de Pago](Figuras/Distribución%20Ticket%20por%20Medio%20de%20Pago.png)

**Evolución mensual de transacciones e importe total por medio de pago:** Se observa una tendencia creciente en el impoprte y tyransacciones asociado a pago con QR, miestras que el resto de los medios de pago tiene un comportamiento erratico en el tiempo, con caidas y picos, tanto en importe como transacciones.

![Evolución Temporal Transacciones-Importe por Medio de Pago](Figuras/Evolución%20Temporal%20Transacciones-Importe%20por%20Medio%20de%20Pago.png)

## 5. Métricas por Ciudad

A partitr del dataframe `df_consolidado` se construyo el dataframe `metricas_ciudad` conteniendo las siguientes columnas: n_transacciones (número transacciones),importe_total, ticket_promedio, desviacion_estandar, n_clientes_unicos, n_productos_vendidos', primera_venta, ultima_venta

El dataframe `metricas_producto` se guardo como archivo CSV llamado `metricas_ciudad.csv`.

**Ciudades por volumen de ventas: (por importe total, descendente)**

|---------------------------------------------------------------------------------------------------------------------|
| Ciudad         | N° Clientes | % del Total |Importe Total ($) | % del Total | N° Transacciones |Ticket Promedio ($) |
|----------------|-------------|-------------|------------------|-------------|------------------|--------------------|
| Rio Cuarto     | 18          | 26.9%       | 792,203          | 29,9%       | 37               | 21,410.9           |
| Alta Gracia    | 14          | 20,9%       | 491,504          | 18,2%       | 25               | 19,260.2           |
| Cordoba        | 11          | 16,4        | 481,482          | 18.2%       | 24               | 20,061.8           |  
| Carlos Paz     |  9          | 13,4        | 353,852 	        | 13,3%       | 13               | 27,219.4           |
| Villa Maria    |  8          | 11,9        | 313,350          | 11,8%       | 11               | 28,486.4           |
|Mendiolaza      |  7          | 10,4        | 229,026          | 8,6%        | 10               | 22,902.6           |      
|---------------------------------------------------------------------------------------------------------------------|

La relación entre número de clientes y volumen de ventas es positiva, con algunas ciudades destacadas tanto en ingresos como en ticket promedio.

![Volumen de ventas por Ciudad](Figuras/Volumen%20de%20ventas%20por%20Ciudad.png)
![Número de Clientes Activos por Ciudad](Figuras/Número%20de%20Clientes%20Activos%20por%20Ciudad.png)
![Relación entre N Clientes y Volumen de Ventas por Ciudad](Figuras/Relación%20entre%20N%20Clientes%20y%20Volumen%20de%20Ventas%20por%20Ciudad.png)

**Distribución de Importes de Ventas por Ciudad:** Se observa que Carlos Paz y Villa María presentan importes medios (ticket promedio por ciudad) mayores al resto de las ciudades, como se aprecia en la tabla anterior (ver ticket promedio por transcción). 

![Distribución de Importes de Venta por Ciudad](Figuras/Distribución%20de%20Importes%20de%20Venta%20por%20Ciudad.png)

## 6. Segmentación de Clientes

Se realizó una segmentación basada en valor total de compras, frecuencia y ticket promedio, clasificando a los clientes en cuatro segmentos:

- **VIP:** Alto valor y alta frecuencia (top 25%)
- **Premium:** Alto valor o alta frecuencia con ticket alto
- **Regular:** Valor medio o frecuencia regular
- **Básico:** Valor bajo y baja frecuencia

A partir del dataframe `metricas_clientes` se construyó el dataframe `clientes_segmentados` generando una nueva columna `segmento` con la clasificación de cada cliente según los criterios mencionados.

**Distribución de clientes e ingresos por segmento (por n° clientes, descendente):**

|------------------------------------------------------------------------------------------------------|
| Segmento | N° Clientes | Importe Total ($) | % Ingresos | Frecuencia Promedio* | Ticket Promedio ($) |
|----------|-------------|-------------------|------------|----------------------|---------------------|
| Básico   | 29          | 618,135           | 23.3%      |  61.5                | 17,573.5            |
| Regular  | 21          | 789,970           | 30.1%      |  44.8                | 25,208.3            |
| Premium  | 13          | 936,935           | 35.3%      |  59.9                | 32,314.4            |
| VIP      |  4          | 297,377           | 11.2%      |  12.8                | 28,942.9            |
|------------------------------------------------------------------------------------------------------|
* Frecuencia Promedio: Días promedio entre compras

Aunque los segmentos VIP y Premium constituyen una menor proporción de clientes, aportan una parte significativa de los ingresos totales (46.5%) y posen un ticket promedio más elevado al resto de los segmentos. Los segmentos Regular y Básico, aunque generan menos ingresos por cliente, son importantes para la base de clientes y ofrecen oportunidades de crecimiento para estrategias de negocio futuras.

![Características por Segmento Figuras](Figuras/Características%20por%20Segmento%20Figuras.png)
![características por Segmento Tabla](Figuras/características%20por%20Segmento%20Tabla.png)
---

# Insights y Conclusiones Clave

A partir deel análisis integral de los datos, se identifican las siguientes conclusiones y oportunidades estratégicas para el negocio:

1. **Activación y retención de clientes:** El 67% de los clientes realizaron compras, pero existe un 33% inactivo con alto potencial de reactivación. Es clave diseñar campañas personalizadas para reincorporar estos clientes y aumentar la base activa. Además, se recomienda analizar las causas de inactividad y estimular su retorno con incentivos específicos.
2. **Dominancia y oportunidad en categorías:** Alimentos es la principal fuente de ingresos y volumen. Por su parte, existen productos que no se vendieron (5) en el periodo analizado, y la categoría Limpieza y productos de mayor margen presentan oportunidades de crecimiento. Es fundamental diversificar la oferta, estimular la venta de productos distintos a alimentos y analizar por qué ciertos productos no tuvieron demanda, ajustando la estrategia comercial.
3. **Transformación digital en pagos:** Aproximadamente el 70% de las transacciones se realizan por medios electrónicos, especialmente QR. Facilitar aún más el pago digital y promover su uso puede mejorar la experiencia del cliente y aumentar la conversión. Se recomienda evaluar alianzas con plataformas de pago y ofrecer incentivos para el uso de medios electrónicos.
4. **Expansión geográfica y campañas focalizadas:** El negocio está concentrado en pocas ciudades, pero existe margen para crecer en localidades con menor volumen de ventas. Realizar campañas de atracción en ciudades con importe más bajo permitirá captar nuevos clientes y diversificar ingresos.
5. **Segmentación estratégica y desarrollo de cartera:** Los segmentos VIP y Premium, aunque minoritarios, generan casi la mitad de los ingresos y muestran tickets promedio elevados. Es recomendable aumentar la cartera de clientes Premium y VIP en zonas geográficas con bajo volumen de ventas, mediante acciones de valor y fidelización diferenciada. Los segmentos Regular y Básico son fundamentales para la estabilidad y crecimiento futuro, por lo que deben ser objetivo de programas de fidelización y desarrollo.
6. **Oportunidades de negocio:**
    - Reactivar clientes inactivos mediante campañas personalizadas y ofertas exclusivas.
    - Analizar y estimular la venta de productos que no se vendieron, ajustando la oferta y comunicación.
    - Impulsar la venta de productos de mayor margen y la categoría Limpieza con bundles y promociones.
    - Fortalecer la presencia en ciudades menos desarrolladas comercialmente, adaptando la oferta a las características locales y realizando campañas de atracción.
    - Desarrollar programas de fidelización diferenciados por segmento, premiando la recurrencia y el ticket promedio.
    - Diversificar la canasta de productos, promoviendo la venta de categorías distintas a alimentos para aumentar el importe promedio.
    - Para productos con precio unitario alto, evaluar la oferta de promociones para estimular su venta.

**En síntesis:** El análisis integral de datos permite identificar palancas claras para maximizar el crecimiento y la rentabilidad: activar clientes inactivos, diversificar categorías y productos, expandirse geográficamente, facilitar el pago electrónico y profundizar la segmentación para acciones comerciales más efectivas.

# Machine Learning y Modelos Predictivos/Clasificación

## Preparación de Datos para Modelos Predictivos/Clasificación

Para la construcción de modelos predictivos/clasificación, se prepararon los datos a partir del dataframe consolidado (`df_consolidado`). 

- En primer lugar, en el archivo `KPI_Reportes.ipynb` se procedió a agregar el segmento de clientes al dataframe `df_consolidado`, mediante una fusión (merge) con el dataframe `clientes_segmentados`, utilizando la columna `id_cliente` como clave, dando lugar al dataframe `df_consolidado_segmentado`.
- En segundo lugar, se eliminó la columna `categoria_corregida` del dataframe `df_consolidado_segmentado`, ya que se consideró que era irrelevante para los modelos.
- En tercer lugar, se creó el data frame `df_clientes_ml` a partir del dataframe `df_consolidado_segmentado`, agrupando por `id_cliente` y calculando las siguientes métricas agregadas para cada cliente:

    * Identificación del cliente: `nombre_cliente`, `email`, `ciudad`
    * Métricas de valor y volumen: `total_compras`, `importe_total`, `ticket_promedio`
    * Métricas de comportamiento y tiempo: `primera_compra`, `ultima_compra`,`dias_entre_compras`,`frecuencia_compra`
    * Métricas de variedad de productos:`productos_diferentes`, `categorias_diferentes`
    * Segmentación: `segmento`

Esto dio lugar a un dataframe de 67 filas y 13 columnas, donde cada fila representa un cliente único con sus respectivas métricas agregadas, incluyendo el segmento al que pertenece (Básico, Regular, Premium o VIP).

- En cuarto lugar, mediante el método reset_index(), se reindexó el dataframe `df_clientes_ml` para asegurar que `id_cliente` fuera una columna regular y no el índice del dataframe.
- Finalmente, se guardó el dataframe `df_clientes_ml` en un archivo CSV llamado `df_clientes_ml.csv` para su posterior uso en la construcción de modelos predictivos/clasificación.

## Carga de Datos Y Procesamiento para Modelos Predictivos/Clasificación

En el notebook `Machine_Learning.ipynb`, el primer paso consistió en la carga y preparación de los datos para los modelos.

1.  **Carga de Datos:** Se cargó el conjunto de datos `df_clientes_ml.csv`, que fue previamente procesado y guardado, en un dataframe de pandas llamado `df`.

2.  **Manejo de Valores Faltantes:** Se identificaron valores nulos en la columna `frecuencia_compra`. Esto ocurre en clientes que solo han realizado una compra. Para solucionar esto, se decidió imputar estos valores nulos con un número alto, calculado como el valor máximo de frecuencia existente más 100 días. Esto representa a clientes con una frecuencia de compra muy baja o no recurrente.

3.  **Ingeniería de Características (Feature Engineering):** La variable categórica `ciudad` no puede ser utilizada directamente por los modelos de machine learning. Por lo tanto, se transformó en variables numéricas utilizando la técnica de "one-hot encoding" (`pd.get_dummies`). Esto crea nuevas columnas para cada ciudad (ej. `ciudad_Cordoba`, `ciudad_Rio Cuarto`), donde un valor de `1` indica que el cliente pertenece a esa ciudad y `0` en caso contrario. Se utilizó el parámetro `drop_first=True` para evitar la multicolinealidad entre las nuevas columnas.

4.  **Análisis de Correlación:** Finalmente, se generó un mapa de calor para visualizar la matriz de correlación entre las variables numéricas más importantes (`importe_total`, `total_compras`, `dias_entre_compras`, etc.). Este análisis es útil para entender las relaciones lineales entre las variables antes de construir los modelos.

![Mapa de Calor Correlación entre Variables Numéricas](Figuras_ml/Mapa%20de%20Calor%20Correlación%20entre%20Variables%20Numéricas.png)

## Modelo 1: Regresión Lineal para Predicción de Importe

1.  **Objetivo:** Predecir el `importe_total` de compra de un cliente. Este es un problema de **predicción**.

2.  **Algoritmo Elegido:** Se utilizó una **Regresión Lineal**. Este modelo es una excelente primera aproximación para problemas de regresión por su simplicidad, interpretabilidad y rapidez. Permite entender la relación lineal entre las variables de entrada y el valor a predecir.

3.  **Entradas (X) y Salida (y):**
    *   **Entradas (X):** Se seleccionaron variables de comportamiento del cliente (las de mayor correlación con `importe_total`): `total_compras`, `dias_entre_compras`, `productos_diferentes`, `categorias_diferentes`, y las columnas de `ciudad` codificadas (one-hot encoding).
    *   **Salida (y):** La variable objetivo a predecir fue `importe_total`.

4.  **Métricas de Evaluación:**
    *   **MAE (Error Absoluto Medio):** Mide la magnitud promedio de los errores en las predicciones, sin considerar su dirección.
    *   **RMSE (Raíz del Error Cuadrático Medio):** Similar al MAE, pero penaliza más los errores grandes. Se expresa en las mismas unidades que la variable objetivo (en este caso, pesos).
    *   **R² Score (Coeficiente de Determinación):** Indica la proporción de la varianza en la variable de salida que es predecible a partir de las variables de entrada. Un valor de 1.0 es perfecto.

5.  **Modelo ML Implementado:** Se implementó el modelo utilizando la clase `LinearRegression` de la biblioteca Scikit-learn.

6.  **División Train/Test y Entrenamiento:** El conjunto de datos se dividió en un 70% para entrenamiento y un 30% para pruebas (`test_size=0.3`). El modelo se entrenó con los datos de entrenamiento.

7.  **Predicciones y Métricas Calculadas:**
    *   **RMSE:** $17,447.24. En promedio, las predicciones del modelo se desvían unos $17,447 del valor real.
    *   **R² Score:** 0.2828. El modelo solo es capaz de explicar el 28.3% de la variabilidad en el `importe_total`.

8.  **Resultados en Gráficos:** Se generó un gráfico de dispersión que compara los importes reales (`y_test_r`) con los importes predichos (`y_pred_r`). La dispersión de los puntos alrededor de la línea ideal (roja) muestra visualmente la modesta capacidad predictiva del modelo.

![Evaluación Regresión Ventas Reales vs Predichas](Figuras_ml/Evaluación%20Regresión%20Ventas%20Reales%20vs%20Predichas.png)

9.  **Conclusiones:** El modelo de Regresión Lineal tiene un poder predictivo limitado para estimar el `importe_total`. El bajo R² y el alto error promedio (RMSE) sugieren que las variables seleccionadas, aunque relevantes, no tienen una relación puramente lineal con el gasto total. Para mejorar la predicción, se podrían explorar modelos no lineales o añadir características más complejas. Otro factor imprte que pudo afectar la caldiad del modelo es la cantidad limitada de datos (67 clientes), lo que restringe la capacidad del modelo para aprender patrones significativos.

## Modelo 2: Regresión Logística para Clasificación de Segmentos

1.  **Objetivo:** Clasificar a un cliente en uno de los cuatro segmentos predefinidos (`Básico`, `Regular`, `Premium`, `VIP`). Este es un problema de **clasificación**.

2.  **Algoritmo Elegido:** Se utilizó una **Regresión Logística Multiclase**. Se eligió este algoritmo porque es eficiente y capaz de manejar problemas de clasificación con más de dos categorías. Además, es un modelo que, aunque más complejo que la regresión lineal, sigue siendo interpretable.

3.  **Entradas (X) y Salida (y):**
    *   **Entradas (X):** Se utilizaron métricas clave que definen el valor del cliente: `importe_total`, `frecuencia_compra`, `ticket_promedio`, `productos_diferentes`, `categorias_diferentes`, y las columnas de `ciudad`. Los datos fueron estandarizados con `StandardScaler` para que todas las variables tuvieran la misma escala, algo importante para este tipo de modelo.
    *   **Salida (y):** La variable objetivo fue `segmento`, codificada numéricamente (ej. 0 para 'Básico', 1 para 'Premium', etc.).

4.  **Métricas de Evaluación:**
    *   **Accuracy (Exactitud):** Porcentaje total de predicciones correctas.
    *   **Classification Report:** Desglose de `precision`, `recall` y `f1-score` para cada segmento, lo que permite evaluar el rendimiento del modelo en cada clase individualmente.
    *   **Confusion Matrix (Matriz de Confusión):** Visualiza los aciertos y errores del modelo, mostrando cuántas veces una clase fue confundida con otra.

5.  **Modelo ML Implementado:** Se usó la clase `LogisticRegression` de Scikit-learn, configurada para clasificación multiclase (`multi_class='multinomial'`).

6.  **División Train/Test y Entrenamiento:** El conjunto de datos se dividió en un 80% para entrenamiento y un 20% para pruebas (`test_size=0.2`).

7.  **Clasificación y Métricas Calculadas:**
    *   **Accuracy:** 71.43%. El modelo acierta en la clasificación de aproximadamente 7 de cada 10 clientes.
    *   **Reporte de Clasificación:**
        *   El modelo funciona bien para las clases `Básico` y `Regular`.
        *   Tiene dificultades con la clase `Premium` (precisión del 50%).
        *   Falla completamente en identificar a los clientes `VIP` (0% en todas las métricas), probablemente debido a la poca cantidad de ejemplos de esta clase en el conjunto de prueba.

8.  **Resultados en Gráficos:** Se generó una matriz de confusión que muestra visualmente los aciertos (diagonal principal) y los errores. Por ejemplo, se puede ver que el modelo confundió a algunos clientes 'Premium' con 'Regular'.

![Matriz de Confusión Aciertos y Errores por Segmento LR](Figuras_ml/Matriz%20de%20Confusión%20Aciertos%20y%20Errores%20por%20Segmento%20LR.png)

9.  **Conclusiones:** El modelo de Regresión Logística tiene una precisión general aceptable, pero su rendimiento es desigual entre las clases. Es bueno para distinguir los segmentos de menor valor, pero no es fiable para identificar a los clientes más valiosos (`Premium` y `VIP`). Esto indica que se necesita más datos de estos segmentos o un modelo más sofisticado para capturar sus patrones.

## Modelo 3: Árbol de Decisión para Clasificación de Segmentos

1.  **Objetivo:** Clasificar a un cliente en un segmento, con el beneficio adicional de generar **reglas de negocio claras e interpretables**. Este es un problema de **clasificación**.

2.  **Algoritmo Elegido:** Se utilizó un **Árbol de Decisión**. Este modelo es ideal cuando la interpretabilidad es una prioridad. Funciona creando una serie de reglas de "si... entonces..." que imitan el razonamiento humano, lo que lo hace muy valioso para la toma de decisiones de negocio.

3.  **Entradas (X) y Salida (y):**
    *   **Entradas (X):** `importe_total`, `ticket_promedio`, `frecuencia_compra`, `productos_diferentes`, y las columnas de `ciudad`.
    *   **Salida (y):** La variable objetivo fue `segmento`, utilizando las etiquetas de texto directamente para que el árbol resultante fuera fácil de leer.

4.  **Métricas de Evaluación:**
    *   **Accuracy (Exactitud):** Porcentaje total de predicciones correctas.

5.  **Modelo ML Implementado:** Se usó la clase `DecisionTreeClassifier` de Scikit-learn, con una profundidad máxima de 3 niveles (`max_depth=3`) para evitar el sobreajuste y mantener las reglas simples y legibles.

6.  **División Train/Test y Entrenamiento:** El conjunto de datos se dividió en un 80% para entrenamiento y un 20% para pruebas.

7.  **Clasificación y Métricas Calculadas:**
    *   **Accuracy:** 85.71%. Este modelo superó significativamente a la Regresión Logística en términos de precisión.
    *   **Reglas del Árbol:** El modelo generó un conjunto de reglas claras. Por ejemplo:
        *   `Si importe_total > 53402.50 Y frecuencia_compra <= 25.35 ENTONCES el cliente es VIP.`
        *   `Si importe_total <= 34783.00 ENTONCES el cliente es Básico o Regular.`

8.  **Resultados en Gráficos:** Se generó una visualización gráfica del árbol de decisión, que muestra cómo el modelo toma decisiones en cada nodo basándose en las variables de entrada.

![Árbol de Decisión Reglas para Segmentar Clientes](Figuras_ml/Árbol%20de%20Decisión%20Reglas%20para%20Segmentar%20Clientes.png)

9.  **Conclusiones:** El Árbol de Decisión no solo fue el modelo más preciso (85.71%), sino también el más valioso desde una perspectiva de negocio. Proporciona una "caja blanca" que revela la lógica detrás de la segmentación, identificando `importe_total` y `frecuencia_compra` como los factores más decisivos. Estas reglas pueden ser implementadas directamente en sistemas de CRM o en estrategias de marketing para clasificar nuevos clientes de forma automática y aplicar acciones comerciales personalizadas.


FIN DOCUMENTACIÓN.