import requests
URL_PRODUCTOS = https://dummyjson.com/products

PRODUCTOS_EJEMPLO = [
    {
        "id": 1, "title": "Router", "category": "redes",
        "price": 80.0, "stock": 2, "rating": 2.5,
        "tags": ["wifi", "redes"],
        "dimensions": {"width": 20, "height": 5, "depth": 15},
        "reviews": [{"rating": 5}, {"rating": 3}, {"rating": 4}],
    },
    {
        "id": 2, "title": "Switch", "category": "redes",
        "price": 120.0, "stock": 0, "rating": 4.1,
        "tags": [], "dimensions": {}, "reviews": [],
    },
    {
        "id": 3, "title": "UPS", "category": "energia",
        "price": 100.0, "stock": 9, "rating": 4.5,
        "tags": ["rack"], "dimensions": {},
        "reviews": [{"rating": 2}, {"rating": 5}],
    },
]

def obtener_productos(limite=10):
    """Consulta DummyJSON y devuelve la lista 'products'.

    Propaga RequestException si falla HTTP o la conexión y ValueError si
    la respuesta no contiene la estructura esperada.
    """
    if not isinstance(limite, int) or isinstance(limite, bool) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo")

    respuesta = requests.get(
        URL_PRODUCTOS,
        params={"limit": limite},
        timeout=10,
    )
    respuesta.raise_for_status() #  Si servidor devuelve error lanza excepción HTTPError
    datos = respuesta.json()

    if not isinstance(datos, dict) or not isinstance(datos.get("products"), list):
        raise ValueError("Respuesta inesperada: falta la lista 'products'")

    return datos["products"]