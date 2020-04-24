#imprimir variables en una cadena

nom = "gerardo"
espacio = (" ")
nom = nom.upper()
print("buenos dias" + espacio + nom)

#.format //toma pocisiones 

nombre = "david"
accion = "puede votar"
edad = 20

print("hola {} , tienes {} , usted {}".format(nombre,edad,accion))

decimales = float(13/5)
print(decimales)
#print("el resultado es {}".format(decimales))
print("el resultado es {r:1.2f}".format(r=decimales))

#format-string
apellido = "sanchez"
nombre1 = "gerardo"
nl =  8

#print(f "hola {nombre1} señor {apellido} su numero de lista es {nl}")

