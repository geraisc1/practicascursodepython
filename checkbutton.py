#Metodo Checkbutton

import tkinter

raiz = tkinter.Tk()
raiz.title("CHECKBUTTON")

#Creamos nuestro metodo checkbutton

def verificar():#Creamos una fincion verificar = command
    valor = check1.get()#agragamos el valor dado
    if (valor==1):
        print("El check esta activo")
    else:                                   #Condiciones
        print("El check se encuentra inactivo")

check1 = tkinter.IntVar()#Activamos nestro check1


boton1 = tkinter.Checkbutton(raiz,text = "opcion1",variable=check1, onvalue = 1, offvalue = 0, command = verificar)#Creamos nuestro checkbutton
boton1.pack()

raiz.mainloop()

#onvalue = valor activo
#offvalue = valor inactivo
