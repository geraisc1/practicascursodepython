#Listas


colores = ["yelow", "blue", "red"]
cantidad = len(colores)
print(cantidad)
print(colores)

cantidad = colores[2]
print(cantidad)

colores[0] = "white"
print(colores)

colores.append("black")
print(colores)

colores.remove("red")
print(colores)

for color in colores:
    print(color)

