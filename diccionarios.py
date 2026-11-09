# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

coche = {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
    "kilometros": 125000
}
#Marca, modelo, color kilometros son claves de la variable coche
# muestra el diccionario completo
print("coche:", coche)

# muestra un elemento con notación []
print('coche["color"]:', coche["color"])
print('coche["kilometros"]:', coche["kilometros"])
# muestra un elemento con método get
print('coche.get("modelo"):', coche.get("modelo"))
print('coche["modelo"]):', coche["modelo"])
#Hay dos formas de acceder a un valor, mediante la clave y mediante el get.
#Pero si el valor no tiene valor el error que da es distinto en ambos, mediante corchetes y clave da un error
# y mediante el get te dice none(no hay valor).

# Recorro los valores del diccionario y sus claves
print("Bucle for que recorre diccionario")
for clave in coche:
    print(" *", clave, "=>", coche[clave])

# Otra forma: items()
# `items()` permite obtener directamente la clave y el valor 
#  en cada iteración. Rn muchos casos resulta más cómodo y legible.
print("Bucle for que recorre diccionario con .items()")
for clave, valor in coche.items():
    print(" - ", clave, "=>", valor)

# Modificar dicccionario 
# con notación []
coche["color"] = "gris"
# con métoddo update
coche.update({"kilometros": 99999}) 
print("coche tras modificaciones:", coche)

# Añadir nuevas claves
coche["taller"] = "Alterio reparaciones"
print("coche tras añadir clave:", coche)

# uso de values() y keys() 
valores = coche.values()
print("valores:", valores)
claves = coche.keys()
print("keys:", claves)

#Los valores y las claves definidas así se actualizan solas por si mismas. Cuando cambiamos algo 
#del diccionario de coche se actualizan solas.

# las variables asignadas con values y keys()
#  se actualizan tras cambios en el diccionario
print('Se añade precio: coche["precio"] = 17000')
coche["precio"] = 17000
print("valores:", valores)
print("keys:", claves)