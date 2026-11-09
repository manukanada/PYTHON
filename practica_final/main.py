from servidores import SERVIDORES, LISTAUNO;
import funciones as f

servidores_encendidos = f.filtrar_por_estado(SERVIDORES, "encendido")
f.mostrar_inventario(servidores_encendidos)

servidores_apagados = f.filtrar_por_estado(SERVIDORES, "apagado")
f.mostrar_inventario(servidores_apagados)

buscar_rol = input("Introduce el rol que vas a buscar: ")
servidores_rol = f.filtrar_por_rol(SERVIDORES, buscar_rol)
f.mostrar_inventario(servidores_rol)