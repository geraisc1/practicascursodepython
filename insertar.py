#incluir datos al fichero

fichero = open("grabacion.txt","at")# con esta funcion abrimos el archivo deseado

datos_fichero = "\nesta es una nueva grabacion"#despues escribimos la informacion que deseamos insertar
fichero.write(datos_fichero)# Y aqui escribimos los datos en el archivo seleccionado
fichero.close()#cerramos el fichero