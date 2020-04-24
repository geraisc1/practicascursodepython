#Expresiones regulares

#search, findall, aplit, sub

texto = "Exepsiones regulares python"
import re #importamos la libreria de expresioones regulares

msj = re.search("python",texto)#agragamos una variable donde tiene el metodo search
print(msj)#en estemetodo se encarga de buscar la palabra deseada en el texto definido

re.search("adios",texto)
resultado = re.search("python",texto)
if (resultado):#Agregamos una condicion en ambos casos de que no encuentre la cadena
    print("Cadena encontrada")
else:
    print("cadena no encontrada")

msj1 = re.search("regulares",texto)
print(msj1)

#findall

texto = """
El pelo de robert es rojo
El pelo de cris es verde
El pelo de andy es verde
"""
msj2 = re.findall("pelo.*verde",texto)#nos permite obtener las palabras relacionadas
print(msj2)#dentro de el texto definido

#aplit

texto = "El celurar es negro y cuesta 2000"
msj3 = re.split("\s",texto)#separa el texto en palabras que lo intregran
print(msj3)

#sub
texto = "El celurar es negro y cuesta 2000"
msj4 = re.sub("negro","blanco",texto)
print(msj4)#Permite remplazar una palabra deseada al texto






