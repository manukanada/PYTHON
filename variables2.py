# Variables, asignación (=) y tipos (int, float, str...) 

saldo_total = 254.55  # float (si a la derecha es un numero decimal es float, 
#si es un numero entero en int
email = 'ana@local.com'  # str
print( "saldo_total") # se va a imprimir lo que esta comillas literalmente
print( saldo_total ) # se va a imprimir la variable saldo_total
    # print(email)   # error indentación

# Tipos
print("tipo de email: ", type(email)  )
print("tipo de saldo_total: ", type(saldo_total)  )
edad = 43
print("Tipo de edad", type(edad), edad*2)

# Variables pueden cambiar de tipo
email = 4
print( "Tipo email: ", type(email)  )
#las variables pueden cambiar de tipo, pero no es nada recomendable hacerlo,
#no deberiamos ir cambiando las variables porque sí, utilizamos otra variables y ya.
print("El email es ", email, " y el saldo es \n", saldo_total, "\n")