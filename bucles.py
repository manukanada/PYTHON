# bucle for básico

# con índices y uso range
# for i in range(5):
#     print(f"{i} ")

# for i in range(5):
#     print(f"{i} ", end=" ")

# for i in range(10, 20):
#     print(f"{i} ", end=" ")

# Suma números
suma = 0  # acumulador

# ini = int(input("inicio: "))
# fin = int(input("fin: "))

# for i in range(ini,fin+1):
#     suma = suma + i
# print("\nSuma:", suma) #\n es el salto de linea para que no aparezca debajo

# while

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    print("Has introducido:", numero)
    numero = int(input("Introduce otro número (0 para terminar): "))

print("Fin del programa")