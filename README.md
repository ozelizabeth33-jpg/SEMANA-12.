# Restaurante App - Semana 12

## Descripción

Este proyecto corresponde a la aplicación `restaurante_app`, desarrollada
para la gestión de productos, usuarios, ventas y control de stock.

En la Semana 12 se mejoraron las búsquedas y consultas mediante el uso de
colecciones auxiliares, principalmente diccionarios (`dict`), manteniendo
las listas principales del sistema.

## Objetivo

Optimizar las búsquedas frecuentes del sistema utilizando índices en
memoria, sin reemplazar las colecciones principales.

## Mejoras realizadas

Se implementaron los siguientes índices:

- `indice_productos`: permite buscar productos mediante su código.
- `indice_usuarios`: permite buscar usuarios mediante su identificación.
- `ventas_por_usuario`: permite consultar las ventas relacionadas con
  cada usuario.

Los índices se reconstruyen automáticamente al iniciar el programa y se
mantienen actualizados cuando se registran datos o se realizan ventas.

## Colecciones utilizadas

Se mantienen las listas principales:

- Lista de productos.
- Lista de usuarios.
- Lista de ventas.

También se utilizan diccionarios como estructuras auxiliares para
optimizar las búsquedas y consultas.

## Persistencia

La información se almacena en archivos JSON:

- `productos.json`
- `usuarios.json`
- `ventas.json`

Los datos se cargan al iniciar el programa y se guardan nuevamente cuando
se realizan cambios.

## Control de stock

Al realizar una venta, el sistema verifica que exista suficiente stock.
Después de confirmar la venta, la cantidad disponible del producto se
actualiza automáticamente.

## Pruebas realizadas

Se comprobó el funcionamiento de:

1. Mostrar productos.
2. Buscar productos por código.
3. Registrar productos.
4. Mostrar usuarios.
5. Buscar usuarios por identificación.
6. Registrar usuarios.
7. Realizar ventas.
8. Consultar ventas por usuario.
9. Actualizar el stock.
10. Cargar y guardar información mediante JSON.

Todas las pruebas realizadas funcionaron correctamente.

## Estructura del proyecto

```text
RESTAURANTE APP NVS/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md