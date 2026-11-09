servidores = [
    {
        "nombre": "web01",
        "ip": "192.168.1.20"
    },
    {
        "nombre": "db01",
        "ip": "192.168.1.30"
    },
    {
        "nombre": "backup01",
        "ip": "192.168.1.40"
    }
]

for x in servidores: 
    print(x)

print(servidores[0])
print(servidores[0]["ip"])

for x in servidores: 
    print(x["ip"])