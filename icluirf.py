#incluir datos al fichero

fichero = open("grabacion.txt","at")

datos_fichero = "\nesta es una nueva grabacion"
fichero.write(datos_fichero)
fichero.close()