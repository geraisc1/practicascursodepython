#Grabar archivos de texto

fichero = open("grabacion.txt","wt")#creamos un nuevo fichero asignandole el nombre y la extencion, con wt

texto = "Hola estoy en facebook" #definimos los datos que va a contener nuestro nuevo fichero

fichero.write(texto)#con este metodo escribimos los datos en el nuevo archivo de texto

fichero.close()#con esta funcion cerramos el archivo para que no que abierto 

