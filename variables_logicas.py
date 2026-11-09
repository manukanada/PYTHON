# lógica o booleana
# importante poner la F y la T de False y True en mayúsculas, sino no funciona.
autorizado = False    # el otro valor posible True
print( type(autorizado)  )

if autorizado==True:  # autorizado==True <=> autorizado (esto esta comparando si la variables es True)
    #importante los dos puntos despues de finalizar la primera línea (condicion)
    print("Puede pasar")
    print("segunda instrucción, aquí iría el código, bla")
else:
    print("No puede pasar")
print("Tras if") #Esto se printea porque está fuera de la condicional, no está dentro de ella al no estar indentada.
#Otra forma de ponerlo es así, el valor True es el default.
# if autorizado:  # autorizado==True <=> autorizado (esto esta comparando si la variables es True)
#     #importante los dos puntos despues de finalizar la primera línea (condicion)
#     print("Puede pasar")
#     print("segunda instrucción, aquí iría el código, bla")
# else:
#     print("No puede pasar")

edad = input("Edad: ") #Todo lo que lee un input es una cadena de caracteres
print(edad, type(edad))
edad = float(edad) #ponemos float en vez de int para evitar los errores al poner decimales ej:21.5
print(type(edad))
if edad==21:  
    print("edad igual a 21")
else:
    print("edad distinto de 21")

#Otro ejemplo
if 21 < edad < 25:  #Otra forma es if 21<edad and edad<25: 
    print("edad entre 21 y 25")
else:
    print("menor de 21 o mayor de 25")

print(edad +1)
print(edad *2)
print(edad /4)

saldo = 100000
edad = 16 

if (edad > 18 or saldo > 50000):
    print("Puede apostar")
