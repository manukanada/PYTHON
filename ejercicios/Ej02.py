#Ejercicio 1
edad = int(input("Edad: "))

if edad == 18 or edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 2
numero = int(input("Escribe un numero: "))

if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else: 
    print("cero")

#Ejercicio 3

edad = int(input("Edad: "))
saldo = int(input("Saldo: "))

if edad > 17 and saldo > 0:
    print("Puede pasar")
else:
    print("No puede pasar")

#Ejercicio 4 
numero1 = float(input("Numero 1: "))
numero2 = float(input("Numero 2: "))

if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero2 > numero2:
    print(numero2, "es mayor que", numero1)
else:
    print("ambos son iguales")