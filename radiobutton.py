#CREAREMOS UN RADIO BUTTON

import tkinter

raiz = tkinter.Tk()
raiz.title("RADIO BUTTON")

#crearemos nuestro radiobutton

#crearemos una funcion para mostrar la accion

def accion():#Creamos nuestra funcion accion
    print("Estas son las opciones {}".format(opcion.get()))#imprimimos un mensaje con nuestra opcion
opcion = tkinter.IntVar()#Creamos nuestro metodo opccion

#CREAMOS NUESTROS RADIOBUTTONS (PARAMETROS)

radio1 = tkinter.Radiobutton(raiz, text ="opcion1", variable = opcion, value = 1, command = accion)
radio1.pack()

radio2 = tkinter.Radiobutton(raiz, text ="opcion2", variable = opcion, value = 2, command = accion)
radio2.pack()

radio3 = tkinter.Radiobutton(raiz, text ="opcion3", variable = opcion, value = 3, command = accion)
radio3.pack()


raiz.mainloop()