#Ejemplos de excepciones
#input() y ValueError
#edad= int(input("Edad: "))

# try:
#     edad = int(input("Edad: "))
#     print("Edad:", edad)

# except ValueError:
#     print("Debe introducir un número entero")

#division por cero

try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))

    resultado = a / b
    print("Resultado:", resultado)

except ValueError:
    print("Debe introducir números enteros")

except ZeroDivisionError:
    print("No se puede dividir entre cero")

