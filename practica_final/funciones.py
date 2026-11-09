from servidores import SERVIDORES;

#apartado 1
def mostrar_inventario(lista):
    """Muestra la información básica de los servidores recibidos."""
    #print(servidores)
    print(f"{'ID':<5} {'NOMBRE':<13} {'ROL':<16} {'ESTADO':<10}{'CPU':<6}{'RAM':<6}" )
    print("---------------------------------------------------------")
    for x in lista:
        print(f"{x["id"]} {x["nombre"]} {x["rol"]} {x["estado"]} {x["cpu"]} {x["ram"]}" )
        print(f"{x["id"]:<5} {x["nombre"]:<13} {x["rol"]:<16} {x["estado"]:<10} {x["cpu"]:<6} {x["ram"]:<6}" );


#mostrar_inventario(SERVIDORES)


#apartado 2
# def buscar_por_id(servidores, identificador):
#     for x in servidores:
#         if identificador == x["id"]:
#             return x
#     return None

# id = int(input("identificador: "))
# res = buscar_por_id(SERVIDORES, id)

# if res == None:
#     print("No encontrado")
# else:
#     print("Encontrado")


#Apartado 3
def filtrar_por_estado(servidores, estado):
    """Devuelve una lista con los servidores del estado indicado."""
    lista = []

    for servidor in servidores:
       if servidor["estado"] == estado:
          lista.append(servidor)
    
    return lista

servidores_encendidos = filtrar_por_estado(SERVIDORES, "encendido")
mostrar_inventario(servidores_encendidos)
servidores_apagados = filtrar_por_estado(SERVIDORES, "apagado")
mostrar_inventario(servidores_apagados)

def filtrar_por_rol(servidores, rol):
    """Devuelve una lista con los servidores del rol indicado."""
    lista = []

    for servidor in servidores:
        if servidor["rol"] == rol:
            lista.append(servidor)
        
    return lista


buscar_rol = input("Introduce el rol que vas a buscar: ")
servidores_rol = filtrar_por_rol(SERVIDORES, buscar_rol)
mostrar_inventario(servidores_rol)

