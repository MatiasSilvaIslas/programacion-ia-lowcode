"""Funciones reutilizables para trabajar con un inventario."""
# Este módulo guarda la lógica útil para manejar productos y stock.
# Las funciones se pueden reutilizar desde otros archivos, como main_inventario.py.


def buscar_producto(
    productos: list[dict],
    nombre_buscado: str,
) -> dict | None:
    # Esta función recibe la lista de productos y el nombre que queremos buscar.
    # Devuelve el diccionario completo del producto si existe, o None si no está.
    nombre_normalizado: str = nombre_buscado.strip().lower()
    # Normalizamos el texto para comparar sin importar mayúsculas ni espacios extra.

    for producto in productos:
        # Recorremos cada producto de la lista.
        nombre_producto: str = str(producto.get("nombre", "")).strip().lower()
        # Convertimos el nombre del producto a minúsculas para poder compararlo bien.

        if nombre_producto == nombre_normalizado:
            # Si coincide el nombre, devolvemos ese producto.
            return producto

    return None
    # Si no se encuentra ningún producto, devolvemos None.


def calcular_valor_total(productos: list[dict]) -> float:
    # Esta función calcula cuánto dinero vale todo el stock del inventario.
    # Multiplica el precio de cada producto por la cantidad que hay en stock.

    total: float = 0.0
    # Empezamos con el total en cero.

    for producto in productos:
        # Recorremos cada producto de la lista.
        total += float(producto["precio"]) * int(producto["stock"])
        # Sumamos el valor de cada producto al total general.

    return total
    # Devolvemos el valor total del inventario.


def productos_con_poco_stock(
    productos: list[dict],
    limite: int,
) -> list[dict]:
    # Esta función devuelve todos los productos cuyo stock es menor o igual a un límite.
    # Se usa para detectar artículos con pocas unidades disponibles.
    """Devuelve una lista nueva con los productos de stock bajo."""
    return [
        producto
        for producto in productos
        if int(producto["stock"]) <= limite
    ]
    # La lista de comprensión filtra los productos que cumplen la condición.

# Crear una función llamada `calcular_unidades_totales()` que reciba la lista de productos y devuelva la suma de todo el stock. Luego importala y probala en la celda siguiente.
def calcular_unidades_totales(productos: list[dict]) -> int:
    """Calcula la suma total de unidades en stock."""
    total_unidades: int = 0
    for producto in productos:
        total_unidades += int(producto["stock"])
    return total_unidades