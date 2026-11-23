import funciones2 as f
from productos import LISTA_dummy, PRODUCTOS_EJEMPLO 

lista = f.obtener_productos()
# print(lista)

f.mostrar_productos(lista)
# f.mostrar_productos([])

# texto = input("texto a buscar en el title: ")
# encontrados = f.buscar_por_titulo(lista, texto)
# f.mostrar_productos(encontrados)

res = f.filtrar_productos(lista, "furniture", None, True)
f.mostrar_productos(res)