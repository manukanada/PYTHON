from servidores import SERVIDORES, LISTAUNO;

# #apartado 1
# def mostrar_inventario(lista):
#     """Muestra la información básica de los servidores recibidos."""
#     #print(servidores)
#     print(f"{'ID':<5} {'NOMBRE':<13} {'ROL':<16} {'ESTADO':<10}{'CPU':<6}{'RAM':<6}" )
#     print("---------------------------------------------------------")
#     for x in lista:
#         print(f"{x["id"]} {x["nombre"]} {x["rol"]} {x["estado"]} {x["cpu"]} {x["ram"]}" )
#         print(f"{x["id"]:<5} {x["nombre"]:<13} {x["rol"]:<16} {x["estado"]:<10} {x["cpu"]:<6} {x["ram"]:<6}" );


# #mostrar_inventario(SERVIDORES)


# #apartado 2
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


# #Apartado 3
# def filtrar_por_estado(servidores, estado):
#     """Devuelve una lista con los servidores del estado indicado."""
#     lista = []

#     for servidor in servidores:
#        if servidor["estado"] == estado:
#           lista.append(servidor)
    
#     # return lista
#     # return [ x for x in servidores if x["estado"] == estado] otra forma de hacer lo de arriba x=servidor
#     return lista

# # servidores_encendidos = filtrar_por_estado(SERVIDORES, "encendido")
# # mostrar_inventario(servidores_encendidos)
# # servidores_apagados = filtrar_por_estado(SERVIDORES, "apagado")
# # mostrar_inventario(servidores_apagados)

# def filtrar_por_rol(servidores, rol):
#     """Devuelve una lista con los servidores del rol indicado."""
#     lista = []

#     for servidor in servidores:
#         if servidor["rol"] == rol:
#             lista.append(servidor)
        
#     return lista


# # buscar_rol = input("Introduce el rol que vas a buscar: ")
# # servidores_rol = filtrar_por_rol(SERVIDORES, buscar_rol)
# # mostrar_inventario(servidores_rol)

# if __name__ == '__main__':
#     print("solo se imprime si se invoca el módulo")

#Apartado 4

def calcular_resumen(servidores):
    """Devuelve un diccionario con las estadísticas globales."""
    resultado = {
        "total" : 0,
        "encendidos": 0,
        "apagados" : 0,
        "disponibilidad" : 0
    }

    resultado["total"] = len(servidores)
    le = [x for x in servidores if x["estado"] == "encendido"]
    resultado["encendidos"] = len(le)
    resultado["apagados"] = resultado["total"] - resultado["encendidos"]
    if resultado["total"] == 0:
        resultado["disponibilidad"] = 0.0
    else:
        resultado["disponibilidad"] = 100 * (resultado["encendidos"]/resultado["total"])
    #Apartado 5
    #Calcular media cpu encendidos
    suma = 0
    for servidor in le:
        suma = suma + servidor["cpu"] # suma += s["cpu"]
    resultado["cpu"] = suma / resultado["encendidos"]    
    return resultado



def mostrar_servicios(servidor):
    """Muestra los servicios y su estado en un servidor."""
    servicios = servidor["servicios"]
    for clave in servicios:
        print(f"{clave}: {servicios[clave]}")

def mostrar_servicios_empresa(servidores):
    """Muestra los servicios y su estado de todos los servidores."""
    for x in lista:
        mostrar_servicios(x)

def contar_servicios_inactivos(servidores):
    """Cuenta servicios inactivos en servidores encendidos.
       y lo devuelve comoo resultado"""
    contador = 0
    le = f.filtrar_por_estado(servidores, "encendido")
    for servidor in le:
        for clave, valor in servidor["servicios"].items():
            if valor == "inactivo":
                contador += 1
    return contador

def mostrar_resumen(servidores):
    res = calcular_resumen(servidores)
    #imprimir res como me piden
    print("Total:" , res["total"])
    print("Encendidos:" , res["encendidos"])
    print("Apagados:" , res["apagados"])
    print("Disponibilidad:" , res["disponibilidad"])
    print("Porcentaje CPU:" , res["cpu"])