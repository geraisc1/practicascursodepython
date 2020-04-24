#Programa main()

import modulofichero #Ivocamos el modulo donde esta el codigo a reutilizar

nombre_fichero = "Grabacion1.txt" #Añadimos nuestro nombre de archivo
fichero1 = modulofichero.Fichero(nombre_fichero)#ccreamos un objeto que tendra la clase de nuestro modulo y el metodo grabar

texto = "hola como estas"#Texto deseado para grabar

fichero1.Grabar(texto)#Utilizamos el metodo  grabar del mudulofichero


texto = "\nEstoy bien por ahora" #Texto nuevo a insertar
fichero1.Insertar(texto)#Utilizamos nuestro metodo Insertar de el modulofichero

texto_leido = fichero1.Leer()#Utilizamos nuestro metodo Leer de el modulofichero y mostrarlo en pantalla
print(texto_leido)



