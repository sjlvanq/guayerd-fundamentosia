# Tienda Aurelion

### Índice

- [Tema](#tema)
- [Problema](#problema)
- [Solución](#solución)
- [Base de Datos](#base-de-datos)
- [Pasos](#pasos)
- [Diagrama de flujo](#diagrama-de-flujo)
- [Pseudocódigo](#pseudocodigo)
- [Ejecutar programa](#ejecutar-programa)

## Tema

Sistema de visualización y análisis de datos comerciales para la gestión eficiente de ventas y productos en Tienda Aurelion.

## Problema

**Contexto actual:**
- Múltiples fuentes de datos comerciales dispersas
- Ausencia de herramientas de visualización integrada
- Dificultad para identificar patrones de compra
- Limitaciones en el análisis de comportamiento de clientes
- Complejidad en el seguimiento de productos más vendidos

## Solución

Sistema integrado de visualización que:

1. **Procesamiento de Datos**
   - Integra las tablas relacionales del negocio
   - Unifica la información en una estructura coherente
   - Procesa datos de ventas, clientes y productos

2. **Funcionalidades Principales**
   - Visualización de métricas clave de negocio
   - Generación de reportes personalizados
   - Análisis de patrones de compra
   - Seguimiento de productos destacados
   - Identificación de clientes frecuentes

3. **Beneficios**
   - Toma de decisiones basada en datos
   - Mejora en la gestión de inventario
   - Optimización de estrategias de venta
   - Seguimiento efectivo del rendimiento comercial

## Base de Datos

1. Fuente

Los datos han sido extraídos del sistema interno de gestión de ventas de la Tienda Aurelion. La información se actualiza diariamente mediante procesos automatizados que garantizan la integridad y consistencia de los datos.

2. Definición

El modelo de datos está compuesto por cuatro tablas principales interrelacionadas:

```
VENTAS
+------------+--------------+-----------+----------------+-------+------------+
| id_venta   | fecha        | id_cliente| nombre_cliente| email | medio_pago |
+------------+--------------+-----------+----------------+-------+------------+
  (PK)          DATETIME      (FK)                                ENUM

DETALLE_VENTAS
+------------+-------------+----------------+----------+----------------+---------+
| id_venta   | id_producto | nombre_producto| cantidad | precio_unitario| importe |
+------------+-------------+----------------+----------+----------------+---------+
  (FK)         (FK)                          INT        DECIMAL         DECIMAL

PRODUCTOS
+------------+----------------+------------+----------------+
| id_producto| nombre_producto| categoria  | precio_unitario|
+------------+----------------+------------+----------------+
  (PK)                         VARCHAR      DECIMAL

CLIENTES
+------------+----------------+-------+--------+------------+
| id_cliente | nombre_cliente | email | ciudad | fecha_alta |
+------------+----------------+-------+--------+------------+
  (PK)                                          DATETIME
```

3. Estructura

- Integridad referencial garantizada mediante claves primarias (PK) y foráneas (FK)
- Normalización: Las tablas cumplen con la Tercera Forma Normal (3NF)
- Índices optimizados en campos de búsqueda frecuente
- Tasas de nulidad < 0.1% en campos críticos
- Unicidad garantizada en identificadores

4. Tipo

Clasificación de campos por naturaleza y dominio:

| Tabla          | Numéricos       | Categóricos     | Temporales |
|----------------|-----------------|-----------------|------------|
| Ventas         | id_venta       | medio_pago      | fecha      |
| Detalle_ventas | cantidad, precio| nombre_producto | -          |
| Productos      | precio_unitario | categoria       | -          |
| Clientes       | id_cliente     | ciudad          | fecha_alta |

5. Escala

Métricas de volumen y calidad:

- **Cardinalidad**: 
  * Ventas: ~10,000 registros/mes
  * Productos: ~1,000 items activos
  * Clientes: ~5,000 registros
  * Detalle_ventas: ~50,000 registros/mes

- **Completitud**: >99.9% en campos obligatorios
- **Precisión**: 100% en cálculos monetarios
- **Consistencia**: Validación cruzada entre tablas relacionadas

## Pasos

El programa sigue las siguientes etapas lógicas de ejecución:

1. **Inicialización y Verificación**
   - Verifica la existencia del archivo documentacion.md
   - Inicializa las estructuras de datos necesarias para almacenar el contenido

2. **Lectura y Procesamiento del Documento**
   - Lee el archivo línea por línea
   - Identifica títulos de nivel 2 (marcados con ##)
   - Procesa y almacena el contenido de cada sección

3. **Estructuración del Contenido**
   - Organiza el contenido en secciones
   - Asocia cada título con su contenido correspondiente
   - Mantiene el orden original del documento

4. **Presentación del Menú Interactivo**
   - Muestra las secciones disponibles como opciones numeradas
   - Incluye una opción para salir del programa

5. **Gestión de Interacción**
   - Captura la selección del usuario
   - Valida la entrada para asegurar que sea una opción válida
   - Maneja posibles errores de entrada

6. **Visualización de Contenido**
   - Muestra el título seleccionado con formato destacado
   - Presenta el contenido de la sección elegida
   - Retorna al menú principal para nuevas selecciones

## Diagrama de flujo

Este diagrama representa el flujo básico del programa, dividido en dos bloques principales:
1. El bloque de lectura y procesamiento del archivo, que maneja la carga y estructuración del contenido
2. El bloque de menú interactivo, que gestiona la interacción con el usuario

El diagrama utiliza la notación estándar de diagramas de flujo donde:
- Los óvalos representan inicio/fin
- Los rombos representan decisiones
- Los rectángulos representan procesos
- Los paralelogramos representan entrada/salida de datos

![Diagrama de flujo del programa](programa.diagrama.png)

## Pseudocodigo

El pseudocódigo describe la lógica del programa en un lenguaje natural estructurado, facilitando la comprensión del algoritmo sin atarse a una sintaxis específica de programación. 

Los conceptos clave implementados son:
- Manejo de archivos y excepciones
- Estructuras de control de flujo (bucles y condicionales)
- Estructuras de datos (listas y diccionarios)
- Formateo de texto para la interfaz de usuario

[Ver pseudocodigo](programa.pseudocodigo.md)

## Ejecutar programa

Para ejecutar el programa se requiere:

1. Requisitos del sistema:
   - Python 3.6 o superior
   - Sistema operativo: Linux, Windows o macOS
   - Terminal o línea de comandos

2. Preparación:
   - Asegurar que el archivo documentacion.md existe en el mismo directorio que programa.py
   - Verificar permisos de lectura en documentacion.md

3. Ejecución:
   ```bash
   python3 programa.py
   ```

4. Uso:
   - Seleccionar una opción del menú ingresando el número correspondiente
   - Presionar Enter para confirmar la selección
   - Para salir, seleccionar la opción 0

