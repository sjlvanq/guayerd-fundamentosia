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

Análisis de datos comerciales de una tienda de mercado para mejorar la gestión de ventas y productos.

## Problema

La tienda cuenta con múltiples registros de ventas, clientes y productos, pero no tiene una herramienta que le permita visualizar patrones de compra, identificar productos más vendidos o entender el comportamiento de sus clientes.

## Solución

Desarrollar un programa en Python que integre las tablas de ventas, clientes, detalle_ventas y productos. El programa permitirá analizar los datos, generar reportes y visualizar métricas clave como productos más vendidos, clientes frecuentes y total de ingresos por período.

## Base de Datos

1. Fuente

Datos extraídos del sistema interno de la tienda

2. Definición

-Tabla Ventas:contiene información de cada venta ( id_venta, fecha,id_cliente, nombre_cliente, email, medio_pago).

-Tabla detalle ventas: Contiene información sobre el detalle de cada producto en una transacción (id_venta,	id_producto, nombre_producto, cantidad,precio_unitario, importe)

-Tabla Productos:Contiene el catálogo de cada producto disponible (id_product, nombre_producto, categoria, precio_unitario)

-Tabla clientes: Información sobre datos básicos de los clientes (id_cliente, nombre_cliente, email, ciudad, fecha_alta)

3. Estructura

Cada archivo tiene formato de tabla con columnas bien definidas. Se pueden relacionar mediante claves primarias y foráneas.

4. Tipo

-ventas:Numéricos discretos, cualitativos nominales y ordinales 

-detalle_ventas: Numéricos discretos y continuos, cualitativos nominales.

-clientes:Numéricos discretos, cualitativos nominales y ordinales

-productos: Numéricos discretos y continuos, cualitativos nominales.

5. Escala

- Datos nominales (nombres, email, nombre producto, categorías, medio de pago,fechas ).

- Datos continuos (precios).

- Datos discretos (cantidad).

## Diagrama de flujo

Este diagrama representa el flujo básico del programa:

![Diagrama de flujo del programa](programa.diagrama.png)

## Pseudocodigo

Lógica general del programa expresada en lenguaje natural, sin sintaxis específica.

[Ver pseudocodigo](programa.pseudocodigo.md)

## Ejecutar programa

Para ejecutar el programa abrir por terminal programa.py

