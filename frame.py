#CREACION DE UN FRAME

import tkinter #importamos la libreria que nos ayuda a graficar

raiz = tkinter.Tk()#invocamos a la raiz tk donde se apoyan los demas componentes de programa
raiz.title("Mi Frame")#Agregamos un titulo al programa

#Creamos los componentes frame

frame = tkinter.Frame(raiz)#Invocamos y creamos nuestro frame
frame.config(bg="black",width = 400, height = 300)#Configuramos nuestro frame
frame.pack()#Mostramos en pantalla

raiz.mainloop() #cerramos


