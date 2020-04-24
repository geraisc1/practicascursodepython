#operardores de identidad (is, is not)

frutas1 = ["manzana", "pera"]
frutas2 = ["mango","sandia"]
frutas3 = frutas1
print(frutas3)

operador_is = frutas3 is frutas1
print(operador_is)

frutas3.append("naranja")

print(frutas3)
print(frutas1)

operador_is_not = frutas3 is not frutas1
print(operador_is_not)






