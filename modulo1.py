#Agregamos la clase coches
class Coches:

    def __init__(self,marca,color,conbustible,cilindrada):
        self.color = color
        self.marca = marca
        self.conbustible = conbustible
        self.cilindrada = cilindrada

    def Mostrar_Caracteristicas(self):
        print("Es color es {} de marca {} conbustible de {} y con cilindrada de {}".format(self.color,self.marca,self.conbustible,self.cilindrada))


#Agregamos la funcion lambda

media = lambda not1,not2,not3 : (not1 + not2 + not3) / 3 #Obtenemos la media con la funcion lambda

