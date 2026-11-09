#Ejercicio 1

servidor = {
    "nombre": "web",
    "ip": "10.10.10.10",
    "puerto": 80
}
print (servidor)

#Ejercicio 2

usuario = { 
    "nombre": "Ana",   
    "edad": 21,   
    "activo": True
}

print("Nombre del usuario: ", usuario["nombre"])
print("Edad del usuario: ", usuario["edad"])
print(usuario["activo"])

if usuario["activo"] == True: #usuario["activo"]:
    print("El usuario está activo")
else:
    print("El usuario está desactivado")

#Ejercicio 3
#Cambiar la IP
servidor["ip"] = "8.8.8.8"
#Añadir clave email
servidor["email"] = "ana@local.com"
#imprimir
print(servidor)

usuario["edad"] = 22
usuario["email"] = "email@local.com"
print(usuario)

#Ejercicio 4

clave= input("Clave a buscar: ")

if clave in servidor:
    print(f"clave {clave} con valor {servidor[clave]}")
else:
    print(f"clave {clave} no existe")

equipo = {  
    "hostname": "server01",   
    "ip": "192.168.1.10",   
    "so": "Linux"
}

if clave in equipo:
    print(equipo[clave])
else:
    print(f"clave {clave} no existe")

#Ejercicio 5
puertos = {   
    "ssh": 22,   
    "http": 80,   
    "https": 443
}

for clave, valor in puertos.items():
    print(clave, "=>", valor)

for clave, valor in servidor.items():
    print(clave, "=>", valor)

for x in servidor:
    print(x, "=>", servidor[x])

#Ejercicio 6
persona = {
    "nombre": "Luis",
    "ciudad": "Cádiz"
}
print(persona.get("nombre"))
print(persona.get("telefono","No disponible"))
