# Ejemplo uso format en print
nombre = "Alfredo Zumberg"
edad = 23
altura = 1.915
print(nombre, "su edad es", edad, "y altura", altura)
# con format(cadenas con formato, es mucho más cómodo que en la de arriba aunque no lo parezca)
print(f"{nombre} su edad es {edad} y altura {altura:.1f}") #lo de la altura es para que redondee a 1 decimal, dos serian :.2f


# Algunos métodos de string

saludo = "Hola Mundo"
print("saludo:", saludo)

print("saludo,lower():", saludo.lower()) #esto hace que saludo aparezca en minusculas pero por supuesto, no la modifica.
#Los metodos=
print("saludo:", saludo)
# No modifica cadena original. 
# Si queremos modificar hace falta asignación

saludo = saludo.lower()
print("saludo:", saludo)

# Replace, lo mismo..
print("saludo.replace():", saludo.replace("mundo", "universo"))
print("saludo:", saludo)

# str como array o lista, longitud o tamaño del str
saludo ="¡Hola mundo!"
print("Primer carácter:", saludo[0]) #En las listas el primer elemento es el 0.
print("Segundo carácter:",saludo[1])
print("Longitud saludo:", len(saludo)) #len es la longitud de la cadena de lenght 

# Buscar en un str: in y not in

texto = "The best thiNgs life are free!"
busca = "FREE"

if busca.lower() in texto.lower(): #Si queremos que sea keysensitive quitamos lo del lower para diferenciar mayus de minus.
    print("¡¡Sí está!!")
else:
    print("No está")

# o en negativo
if busca not in texto:
    print("No está")
else:
    print("¡¡Sí está!!") 
# Proponer: no case sensitive


# Concatenar str

nombre = "Raquel"
apellidos = "García Ross"
print(nombre + " " + apellidos) 

nombreCompleto = apellidos + ", " + nombre #Esta forma le gusta mas a Ango
print(nombreCompleto) 

# Recorrer str
for x in nombre: #Para cada caracter en la variable nombre, imprime caracter
    print(x)

# con índices
for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")
    print(f"nombre[{i}]: {nombre[i]}")
