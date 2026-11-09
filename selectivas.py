## Selectiva simple (y  probar indentación)

edad = int(input("Edad: "))
print( type(edad) ) 

if  edad >= 18:  # selectiva simple
    print("Adulto")
    print("puede jugar") ## Error indentación
print("¡Hola Clase!")  # siempre,fuera if




# Ejemplo selectiva if-else y condición lógica con and

saldo = int(input("saldo: "))
edad = int(input("edad: "))

if (edad >= 18 and saldo > 0) or (saldo >100000):
    print("Puede jugar")
else:
    print("no puede jugar")
print("Fin selectiva")  # siempre,fuera if

#Otra forma de hacerlo
autorizado = (edad >= 18 and saldo > 0) or (saldo >100000)
if autorizado:
    print("Puede jugar")
else:
    print("no puede jugar")

# Ejemplo selectiva anidadas
a = int(input("valor de a:"))
b = 200

if b > a:
    print("b es mayor que a")
else: 
    if b<a:
        print("a es mayor que b")
    else:
        print("son iguales") 

# lo mismo con elif (else if), más legible/compacto
if b > a:
    print("b es mayor que a")
elif b<a:
    print("a es mayor que b")
else:
    print("son iguales")
