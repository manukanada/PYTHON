#ejercicio 1
import os

#ejercicio 2
lista = os.listdir("/tmp")
print(lista)

# for x in lista:
#     print(x)

for i in range(len(lista)):
    print(i, "-", lista[i])

#Ejercicio 3

dir = input("Nombre directorio a crear: ")

os.mkdir("/tmp"+dir)