#Creamos el metodo messagebox

import tkinter #importamos la libreria
from tkinter import messagebox # de tkinter importamos especificamente messagebox

raiz = tkinter.Tk()
raiz.title("Messagebox")

#Creamos nuestro messagebox

def avisar(): #creamos nuestra funcion avisar
    tkinter.messagebox.showinfo("Titulo","Mensaje con la informacion")#confuguramos nuestro messagebox




boton = tkinter.Button(raiz,text = "Pulsar para aviso", command = avisar)#Acemos uso de un boton con la accion avisar
boton.pack()



raiz.mainloop()
