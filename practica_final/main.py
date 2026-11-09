from servidores import SERVIDORES, LISTAUNO;
import funciones as f

# servidores_encendidos = f.filtrar_por_estado(SERVIDORES, "encendido")
# f.mostrar_inventario(servidores_encendidos)

# servidores_apagados = f.filtrar_por_estado(SERVIDORES, "apagado")
# f.mostrar_inventario(servidores_apagados)

# buscar_rol = input("Introduce el rol que vas a buscar: ")
# servidores_rol = f.filtrar_por_rol(SERVIDORES, buscar_rol)
# f.mostrar_inventario(servidores_rol)

# res = f.calcular_resumen(SERVIDORES)
# print(res)

# f.mostrar_resumen(SERVIDORES)
# f.mostrar_resumen(LISTAUNO)

f.mostrar_servicios(SERVIDORES[0])
res = f.contar_servicios_inactivos(SERVIDORES)
print(res)