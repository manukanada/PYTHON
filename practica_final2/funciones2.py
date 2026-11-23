import requests

# URL de la API
URL_PRODUCTOS = "https://dummyjson.com/products"

def obtener_productos(limite=10, skip=10):
    """Consulta DummyJSON y devuelve la lista 'products'.

    Propaga RequestException si falla HTTP o la conexión y ValueError si
    la respuesta no contiene la estructura esperada.
    """
    if not isinstance(limite, int) or isinstance(limite, bool) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo")

    respuesta = requests.get(
        URL_PRODUCTOS,
        params={"limit": limite, "skip": skip},
        timeout=10,
    )
    respuesta.raise_for_status()  #  Si error (400 a 599), excepción HTTPError; si ok devuelve None.
    datos = respuesta.json()

    if not isinstance(datos, dict) or not isinstance(datos.get("products"), list):
        raise ValueError("Respuesta inesperada: falta la lista 'products'")

    return datos["products"]

def mostrar_productos(productos):
    """Imprime un listado compacto sin alterar los datos."""
    if productos: #esto es para comprobar si la lista esta vacia o no
        print(f"{'ID':<4} {'PRODUCTO':<45} {'CATEGORÍA':<16} {'PRECIO':<10} {'STOCK':<6}")
        print("-"*79)

        for p in productos:
            print(f"{p['id']:<4} {p['title']:<45} {p['category']:<16} {p['price']:<10} {p['stock']:<6}")
    else:
        print("No hay elementos en la lista ")


def buscar_por_titulo(productos, texto):
    texto = texto.strip().lower()
    res = []
    for p in productos:
        if texto in p['title'].lower():
            res.append(p)

    return res


def filtrar_productos(productos, categoria=None, precio_max=None, solo_disponibles=False): #a Ango no le gustan este tipo de funciones con ifs continuos
#el hubiera hecho 3 funciones distintas muy sencillas por separado. De hecho es muy probable que la ponga en el examen.

    res = []
    for p in productos:
        if categoria != None:
            categoria = categoria.strip()
        if ( ( categoria == None or categoria == p['category'] ) 
             and ( precio_max == None or precio_max  > p['price'] )
             and ( solo_disponibles == False or p['stock'] > 0 )
           ):
           res.append(p)

    return res