def buscar_producto(
    productos: list[dict],
    nombre_buscado: str
) -> dict | None:
    """Busca un producto por nombre sin distinguir mayúsculas ni espacios externos."""
    nombre_normalizado: str = nombre_buscado.strip().lower()

    for producto in productos:
        nombre_producto: str = str(producto.get("nombre", "")).strip().lower()

        if nombre_producto == nombre_normalizado:
            return producto

    return None


if __name__ == "__main__":
    productos_prueba: list[dict] = [
        {"nombre": "Lámpara", "precio": 25000.0, "stock": 8},
        {"nombre": "Silla", "precio": 45000.0, "stock": 3},
    ]

    # Producto encontrado.
    assert buscar_producto(productos_prueba, "Silla") == productos_prueba[1]

    # Producto inexistente.
    assert buscar_producto(productos_prueba, "Banco") is None

    # Inventario vacío.
    assert buscar_producto([], "Silla") is None

    print("Las tres pruebas se ejecutaron correctamente.")