#Entrada de texto de mas lineas

import tkinter

raiz = tkinter.Tk()
raiz.title("Mis texos")

#Creamos el componente text de varias lineas

entrada = tkinter.Text(raiz)#creamos el componente text
entrada.config(width=20,height=10,font = ("Verdana",15),padx = 10, pady = 10,fg="green", selectbackground="lightgrey")#configuramos el componente text
entrada.pack()


raiz.mainloop()