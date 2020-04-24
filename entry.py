#Entrada de datos por teclado

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi entry")

#Creamos nuestro componente entry(entrada de datos)

entrada = tkinter.Entry(raiz)#creamos la estructura de la entrada de datos
#entrada.config(justify="center")
entrada.config(justify="center",show ="*")#configuramos nuestra entrada de datos como password
entrada.pack()


raiz.mainloop()
