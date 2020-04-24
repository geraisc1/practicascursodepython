#leer ficheros

fichero = open ("Fichero1.txt","rt") #creamos una variable llamada fichero, y con la funcion open abriremos el archivo de texto ya creado, y con (rt) leemos en forma txt

datos_fichero = fichero.read()#creamos la funcion datos_ficheros donde leemos el archivo con el .read()
print("Estos son los datos del archivo de texto {}".format(datos_fichero))#imprimimos los datos que contiene el archivo de texto
