"""Ejemplo de programa principal que utiliza el módulo inventario."""
# Este archivo funciona como punto de entrada del programa.
# Aquí se definen los datos y se llaman a las funciones del módulo inventario.

from inventario import (
    buscar_producto,
    calcular_valor_total,
    productos_con_poco_stock,
)
# Importamos las funciones que vamos a usar desde el módulo inventario.


productos: list[dict] = [
    {"nombre": "Lámpara", "precio": 25000.0, "stock": 8},
    {"nombre": "Silla", "precio": 45000.0, "stock": 3},
    {"nombre": "Mesa", "precio": 120000.0, "stock": 0},
]
# Creamos una lista de productos.
# Cada producto es un diccionario con nombre, precio y cantidad en stock.

print("Búsqueda:", buscar_producto(productos, "silla"))
# Buscamos un producto por nombre y mostramos el resultado.

print(f"Valor total: ${calcular_valor_total(productos):,.2f}")
# Calculamos el valor total del inventario y lo mostramos con formato de moneda.

print("Stock bajo:", productos_con_poco_stock(productos, 3))
# Mostramos todos los productos que tienen un stock igual o menor a 3.
