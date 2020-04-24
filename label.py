#CREAREMOS LA HERRAMIENTA LABEL

import tkinter #importamos libreria

raiz = tkinter.Tk()#creamos el metodo tk(importante)
raiz.title("Mi label")#le ponemos un titulo al frame

#Creamos los componentes del label (etiqueta)

texto = 'Hola Mundo' #definimos una cadena deseada
etiqueta = tkinter.Label(raiz,text=texto)#Creamos nuestro label con los parametros de texto(cadena)
etiqueta.config(fg="green",bg="lightgrey",font = ("Cortana",30))#configuramos nuestro label como se desee
etiqueta.pack()#Mostramos en pantalla

raiz.mainloop()#Cerramos
