import os

# Se invoca dejando los parentesis vacios
directorio_actual = os.getcwd()

print(f"El script se está ejecutando desde: {directorio_actual}")
print(type(directorio_actual))

# dir = input("nombre dir a crear: ")
# os.mkdir(dir)

# Método con argumento opcional
files_dir_actual = os.listdir()
files_dir_asir = os.listdir("/home/asir/python")
print(files_dir_actual)
print(files_dir_asir)

for x in files_dir_asir:
    print(x)



