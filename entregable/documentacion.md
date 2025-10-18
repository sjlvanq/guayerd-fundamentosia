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
Tienda Aurelion es una tienda de mediana o pequeña escala que busca optimizar la gestión y análisis de su información comercial mediante una herramienta visual interactiva basada en archivos Markdown.

## Problema
Actualmente, la tienda carece de una herramienta visual que facilite la consulta estructurada de documentación y datos, dificultando la labor de análisis de negocio y datos, así como la consulta técnica y operativa del software.

## Solución
Se desarrolla un software que presenta el contenido de la documentación en formato Markdown a través de un menú interactivo en consola. El usuario puede navegar por las distintas secciones del documento y consultar información relevante de manera estructurada y accesible.

## Base de Datos
### 1. Fuente
Los datos provienen de archivos CSV generados a partir de hojas de cálculo: `clientes.xlsx.csv`, `productos.xlsx.csv`, `ventas.xlsx.csv` y `detalle_ventas.xlsx.csv`.

### 2. Definición
La base de datos almacena información sobre clientes, productos, ventas y el detalle de cada venta. Permite analizar el comportamiento comercial, la relación entre clientes y productos, y la trazabilidad de las operaciones.

**Relaciones principales:**
- Cada venta (`ventas`) está asociada a un cliente (`clientes`).
- Cada venta puede tener uno o más detalles de venta (`detalle_ventas`), que a su vez referencian productos (`productos`).

### 3. Estructura
**Tabla: clientes**
```
+------------+-------------------+--------------------------+-------------+------------+
| id_cliente | nombre_cliente    | email                    | ciudad      | fecha_alta |
+------------+-------------------+--------------------------+-------------+------------+
```

**Tabla: productos**
```
+-------------+------------------------+-----------+----------------+
| id_producto | nombre_producto        | categoria | precio_unitario|
+-------------+------------------------+-----------+----------------+
```

**Tabla: ventas**
```
+----------+------------+------------+-------------------+--------------------------+-------------+
| id_venta | fecha      | id_cliente | nombre_cliente    | email                    | medio_pago  |
+----------+------------+------------+-------------------+--------------------------+-------------+
```

**Tabla: detalle_ventas**
```
+----------+-------------+------------------------+----------+----------------+---------+
| id_venta | id_producto | nombre_producto        | cantidad | precio_unitario| importe |
+----------+-------------+------------------------+----------+----------------+---------+
```

### 4. Tipo
- Almacén de datos tabular, estructurado en archivos CSV.
- Relaciones de tipo 1:N entre clientes y ventas, y entre ventas y detalle_ventas.
- Integridad referencial basada en claves primarias y foráneas (id_cliente, id_venta, id_producto).

### 5. Escala
- 100 clientes
- 100 productos
- 120 ventas
- Más de 500 registros en detalle_ventas
- Calidad: Sin valores nulos en claves principales, formato consistente, relaciones completas entre tablas.

## Pasos
1. Verificación de existencia del archivo de documentación.
2. Lectura y procesamiento del archivo, identificando títulos de nivel 2 como secciones principales.
3. Estructuración del contenido en una lista de secciones con título, nivel y contenido.
4. Presentación de un menú interactivo en consola, mostrando las secciones disponibles.
5. Recepción y validación de la opción seleccionada por el usuario.
6. Visualización del contenido de la sección elegida, con formato destacado para el título.
7. Repetición del menú hasta que el usuario decida finalizar el programa.

## Diagrama de flujo
![Diagrama de flujo del programa](programa.diagrama.png)
El diagrama ilustra el flujo principal del programa: desde la verificación del archivo, la lectura y estructuración de secciones, hasta la interacción con el usuario mediante el menú y la visualización de contenidos.

## Pseudocodigo
[Ver pseudocodigo](programa.pseudocodigo.md)
El pseudocódigo describe la lógica implementada en el programa, facilitando la comprensión de su funcionamiento y la relación entre las distintas etapas del flujo.

## Ejecutar programa
Para ejecutar el programa, siga estos pasos:

1. Asegúrese de tener instalado Python 3.6 o superior en su sistema.
2. Coloque el archivo `programa.py` y el archivo `documentacion.md` en el mismo directorio.
3. Abra una terminal y navegue hasta el directorio del proyecto.
4. Ejecute el siguiente comando:
   ```bash
   python3 programa.py
   ```
5. Siga las instrucciones en pantalla para seleccionar y visualizar las secciones del documento.

**Notas:**
- No se requieren dependencias externas.
- El programa está diseñado para ejecutarse en sistemas Linux, pero es compatible con cualquier sistema que disponga de Python 3.
- Si el archivo `documentacion.md` no existe, el programa mostrará un mensaje de error y finalizará.
