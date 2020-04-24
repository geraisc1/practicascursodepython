#creacion de el metodo filedialog

import tkinter
from tkinter import filedialog #utilizamos la libreria filedialog

raiz = tkinter.Tk()
raiz.title("Mi FILEDIALOG")

#Creamos nuestra funcion filedialog

def abrirfichero():
    ruta = filedialog.askopenfilename(title = "Abrir fichero")#configuramos una ruta para abrir un archivo
    print(ruta)#imprimimos la ruta en pantalla (Terminal)


#Utilizamos un boton para determinar una accion para el file dialog
buton = tkinter.Button(raiz,text = "Pulsa para empezar",command = abrirfichero)
buton.pack()

raiz.mainloop()

#Permite mostra un dialogo para abrir un archivo por medio de una ruta