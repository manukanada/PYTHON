#ej1
lista_ip= [22, 53, 80, 443, 8080]

print(lista_ip)

for ip in lista_ip:
    print("-", ip)

#ej2
usuarios = ["ana", "luis", "marta"]

print(usuarios)

usuarios[0]="alfredo"
print(usuarios)

usuarios.append("raquel")
print(usuarios)

usuarios.insert(1, "carlos")
print(usuarios)

#ej3
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

buscar = input("introduce la ip: ")

if buscar in ips:
    print("está en la lista") 
else:
    print("no esta en la lista") 

#ej4
try:
    pos = ips.index(buscar) 
    print(f"{buscar} está en la posición {pos}") 
except ValueError:
    print("no existe esa ip en la lista")

#ej5
edades = [34, 18, 55, 21, 40]

edades.sort()
print("edades ordenadas: ", edades)
edades.reverse()
print("edades orden inverso: ", edades)

#ej6
usua=input("introduce usuarios separado por comas: ")

lista = usua.split(",")
print("lista:", lista)

#ej7
nota=input("introduce notas separado por comas: ")
notas=nota.split(",")
suma = 0

for x in notas:
    suma = suma + float(x)
media = suma/len(notas)
print(f"Media: {media:.2f}")

#ej8
numeros = ["10", "20", "30", "40"]

print("numeros:", numeros, "tipo:", type(numeros))
print("type(numeros[0]):", type(numeros[0]))

