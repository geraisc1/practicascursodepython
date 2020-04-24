
#Ejercicio para buscar una palabra apartir de un texto dado

import re #importamos la libreria de expresiones regulares

def buscar(palabra,texto):#creamos la funcion con los parametros de la palabra y el texto
    resultado = re.search(palabra,texto)}#definimos el metodo search para buscar
    return resultado #retornamos el valor

texto = "Esta es una frase de busqueda"
palabra = "frase"

resultado = buscar(palabra,texto)
print(resultado)


    
   