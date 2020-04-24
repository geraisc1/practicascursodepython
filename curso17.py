#Diccionarios

diccionario = {"red":"rojo","yelow":"Amarillo","pink":"Rosa"}
print(diccionario)

color = diccionario["red"]
print(color)

diccionario["black"] = "negro"
print(diccionario)

diccionario.pop("pink")
print(diccionario)

del(diccionario["black"])
print(diccionario)

for color in diccionario:
    print(color)

for clave,valor in diccionario.items():
    print(clave,valor)
    
