
#PROGRAMA MODULO DONDE SE ENCUENTRA EL CODIGO A REUTILIZAR

class Fichero: #Creamos nuestra clase Fichero

    def __init__(self,nombre):#creamos nuestra funcion prinpal, parametros principales
        self.nombre = nombre

    def Grabar(self,texto):#creamos la funcion grabar para crear un nuevo archivo
        fichero = open(self.nombre,"wt")
        fichero.write(texto)
        fichero.close()

    def Insertar(self,texto):#En estafincion insertamos nuevos datos al archivo.txt
        fichero = open(self.nombre,"at")
        fichero.write(texto)
        fichero.close()

    def Leer(self):
        fichero = open(self.nombre,"rt")#Aqui leemos y mostramos en pantalla todos los datos que contiene el archivo.txt
        texto =fichero.read()
        return texto





