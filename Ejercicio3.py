#Ejercio 3

dicinario = {"manzana":"people","platano":"banana","naranja":"orange","limon":"lemon"}
print("DICCCIONARIO DE FRUTA:::", dicinario)

fruta = dicinario["naranja"]#muestra la clave de la naranja
print("la traduccion de la fruta es...." + fruta)

dicinario["piña"] = "pineapple"#agrega un elemento al diccionario 
print(dicinario)

for clave,valor in dicinario.items():#muestra el conjuto de datos con una clave y un valor
    print(clave,valor)
    








