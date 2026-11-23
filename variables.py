# variables.py
login = "manukanada"
password = "1234"
peso = 58.0
jubilado = False
print( "Tipo de login:", type(login), "\n", login ) #str, si quiero poner varios argumentos los tengo que
#separar con comas(,). Login nos pone el tipo de variable. \n nos salta de linea
print( type(peso) ) #float
print( type(password) ) #str
res = type(jubilado) #boolean
print(res) #res es igual a algo por ello cuando print(res) me dice el type de jubilado que es boolean
if peso > 100:
    print("sobrepeso")
else:
    print("ok el peso")
    print(peso)
    print("Despues del if")

