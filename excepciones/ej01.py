import os

os.mkdir("/root/nueva_carpeta")

try:
    os.mkdir("/root/nueva_carpeta")
except PermissionError:
    print("No tiene permisos para crear el directorio")


print("tras bloque try")