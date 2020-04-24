#METODO BUTTON PARA EJECUTAR UNA DETERMINADA ACCION

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi button")#Creamos nuestro programa boton

#creamos nuestro button

#creamos un funcion llamada accion
def accion():
    raiz = tkinter.Tk()
    raiz.title("Mi button")
    texto = 'Hola Mundo' #mostramos un texto en la segunda ventana
    etiqueta = tkinter.Label(raiz,text=texto)
    etiqueta.config(fg="green",bg="lightgrey",font = ("Cortana",30))
    etiqueta.pack()

     

boton = tkinter.Button(raiz,text = "Ejecutar",command = accion)#invocamos la funcion con el text que definimos
boton.config(fg="green")#configuramos el color de el texto del boton
boton.pack()

raiz.mainloop()

#command = ejecuta una accion
#config = configura una accion

