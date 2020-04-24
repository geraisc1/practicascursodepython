#importamos el modulo1 ya antes creado

import modulo1 # importamos el modulo creado donde tenemos nuestro codigo a reutilizar

coche1 = modulo1.Coches("ford","negro","gasolina","2.4")#instancioamos nuestra clase coches y agregamos los parametros
print(coche1.Mostrar_Caracteristicas()) #hacemos uso de nuestro medoto Mostrar_Caracteristicas() de la clase cohes

media = modulo1.media(1,9,10)#instacioamos a la funcion lambda y le agregamos lo parametros a calular

print("La media es {}".format(media))#mostramos el resultado con la variable media





