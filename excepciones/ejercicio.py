#ejercicio.py

#Crear lista y acceder a un valor que no existe

latencias = [1.2, 3.4, 4.5, 16.2, 7]
indice = int(input("Posicion en la lista: "))


try:
    print(latencias[indice])

except IndexError:
    print(f"El valor {indice} está fuera de rango, max {len(latencias)-1}")

#Crear un diccionario y acceder a una clave que no existe

servidor = {
    "nombre" : "adriano",
    "ip" : "192.168.1.53"
}

clave = input("A que clave quieres acceder: ")

try:
    print(servidor[clave])

except KeyError:
    print(f"La clave ̣{clave} no existe")


