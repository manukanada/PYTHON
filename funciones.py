#funciones

# def imprime_linea(tam,cadena): #tenemos la función imprime_linea
#     #y sus argumentos tam y cadena.
#     print(tam*cadena)

# imprime_linea(25,"-")


from utiles import suma_lista, calcula_media


latencias_web = [1.5, 2.3, 4.7, 8.9]
latencias_ftp = [2.5, 3.3, 4.3, 9.9]

def calcula_media (lista):
    suma = 0
    for x in lista:
        suma = suma + x #suma += x
    return suma/len(lista)

media_web = calcula_media(latencias_web)
print("Media Web", media_web)
media_ftp = calcula_media(latencias_ftp)
print("Media ftp", media_ftp)

if media_web > media_ftp:
    print("media web es mayor")
elif media_web < media_ftp:
    print("media ftp es mayor")
else:
    print("ambos son iguales")