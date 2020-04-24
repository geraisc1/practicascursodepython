#ciclo for

colores = ["red","blue","pink","yellow"]
print(colores)

for color in colores:
    print(color)

range(9)
print(range)

for numero in range(8):
    print(numero)
print"hola"
for numero in range(4,8,2):#por cada numero en el rango de dos en dos
    print(numero)

for numero in range(15):
    if numero == 10:
        break
    print(numero)
print"hola"
for numero in range(5):#omite el numero 2 de la lista
    if numero ==2:
        continue
    print(numero)
print"hola" 

for numero1 in range(6):#for anidado
    for numero2 in range(4):
        print(numero1,numero2)




