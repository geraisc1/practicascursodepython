#Clases y objetos (POO)



class Clasesilla:#se cre una clase llamada silla
    presio = 200#son los atributos de la clase
    color = "green"

objectosilla1 = Clasesilla()#se crea un objeto dentro de la clase
objectosilla1.color#pasa parametros de los atributos de la clase al objeto
objectosilla1.presio
print(objectosilla1.color)
print(objectosilla1.presio)

objectosilla2 = Clasesilla()#crea un segundo objeto para la clase
objectosilla2.presio = 300 #añade nuevos atributos al objeto
objectosilla2.color = "Amarillo"

print("segundo objeto con atributos")
print(objectosilla2.presio)
print(objectosilla2.color)

class Personas:#crea una segunda clase llamada personas
    def __init__(self,nombre,edad):#creacion de un metodo o funcion al cual se agregan parametros como nombre y edad
        self.nombre = nombre#parametros.self
        self.edad = edad
    def Saludar(self):#definimos el segundo metodo de nuestra clase

        print("hola me llamo {} y tengo {} años de edad".format(self.nombre,self.edad))


persona1 = Personas("David",30)
print(persona1.edad)
print(persona1.nombre)

print(persona1.Saludar())#invoca el metodo saludar (mandar a llamar)





















