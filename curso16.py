#Conjuntos

conjunto_de_colores = {"white","red","brow"}
print(conjunto_de_colores)

posicion = len(conjunto_de_colores)
print(posicion)

for color in conjunto_de_colores:
    print(color)

conjunto_de_colores.add("black")
print(conjunto_de_colores)

conjunto_de_colores.remove("black")
print(conjunto_de_colores)