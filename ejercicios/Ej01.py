#Ejercicio 1
nombre = "Manuel"
edad = 21
altura = "1,74"

print(nombre, edad, altura)
print("tipo nombre",type(nombre))
print("tipo edad",type(edad))
print("tipo altura",type(altura))

#Ejercicio 2
frase = "Python es divertido"

print(frase.lower())
print(len(frase))

if "python" in frase.lower():
    print("python si esta en la frase")
else:
    print("python no esta en la frase")

print(frase[::-1])

#Ejercicio 3
es_administrador = False

if es_administrador == True:
    print("Acceso de administrador")
else:
    print("Acceso de usuario")

es_administrador = True

if es_administrador == True:
    print("Acceso de administrador")
else:
    print("Acceso de usuario")

#Ejercicio 4
precio = float(input("Precio:" ))
cantidad = float(input("Cantidad: "))

importe = precio * cantidad
print("Importe: ", importe)

#Ejercicio 5
nombre = input("Nombre: ")
anyoNacimiento = float(input("Año de nacimiento: "))

edad = 2026 - anyoNacimiento
print(edad)