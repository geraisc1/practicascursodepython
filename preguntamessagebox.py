#CREAREMOS UN MESSAGEBOX PARA PREGUNTAR

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi question")

#Creamos nuestra funcion 
def pregunta():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","Quieres borrar este fichero")#creamos y configuramos nuestro messagebox.askquestion
    if (resultado == "yes"):
        print("Si quiero borrar el fichero")
    else: #condiciones
        print("No quiero borrar el fichero pleace")


boton = tkinter.Button(raiz,text = "Pulsar para preguntar",command = pregunta)#configuramos nuestro boton con la accion pregunta
boton.pack()



raiz.mainloop()
