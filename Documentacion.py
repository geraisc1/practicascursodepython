#Generar documentacion automaticamente
'''
def saludar(nombre):

    """
    Este es un comentario para la funcion saludadr

    """

    print("Hola  buenos dias  " +  nombre)

saludar("GERA")
'''
#help(saludar)

class Saludar:#creamos una clase saludar
    """
    Esta es una clase que tendra dos funciones buenos_dias y adios
    Ambos parametros tendran como parametro el nombre

    """

    def buenos_dias(self,nombre):#creamos una funcion para saludar

        print("Hola buenos dias {}".format(nombre))#mensaje que mostrara en pantalla

    def adios(self,nombre):#creamos una funcion para despedirnos(adios)

        print("Adios {} ".format(nombre))

saludo = Saludar()
saludo.adios("Gerardo Briseño")#invocamos a la clase Saludar

help(Saludar)#help ayuda a generar la documentacion del programa
#adios("Gerardo Briseño")
 
 #help() = Ayuda a obtener la documentacion de cualquier funcion de python
 


