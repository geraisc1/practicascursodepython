#Ejercicio 5

class Coches:

    def __init__(self,marca,color,conbustible,cilindrada):
        self.color = color
        self.marca = marca
        self.conbustible = conbustible
        self.cilindrada = cilindrada

    def Mostrar_Caracteristicas(self):
        print("Es color es {} de marca {} conbustible de {} y con cilindrada de {}".format(self.color,self.marca,self.conbustible,self.cilindrada))

objectcoches1 = Coches("Opel","rojo","gasolina","1.6")

print(objectcoches1.Mostrar_Caracteristicas())




  
