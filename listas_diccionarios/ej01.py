servidor = {
    "nombre": "web01",
    "ip": "192.168.1.20",
    "servicios": ["ssh", "http", "https"]
}

print("Servidor:", servidor["nombre"])
print("IP:", servidor["ip"])
print("Servidor:", servidor["servicios"])

for x in servidor["servicios"]:
    print(x)

print("Primer servicio: ", servidor["servicios"][0])

servidor["servicios"].append("dns")

for x in servidor["servicios"]:
    print(x)
    