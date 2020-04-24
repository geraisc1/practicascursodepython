#Funciones

def Saludo(Nombre):
    print("BUENOS DIAS" + Espacio + Nombre)
Espacio = (" ")
Nombre = "GERA"
print(Saludo(Nombre))

def Suma(numero1,numero2):
    suma = numero1 + numero2
    return suma
    
numero1 = 10
numero2 = 90
resultado =  Suma(numero1,numero2)
print(resultado)

#paso de valor por referencia

colores = ["red","blue","green","Pink"]
def Colores(colores,color):
    colores.append(color)

color = "black"
print(Colores(colores,color))

print(colores)

