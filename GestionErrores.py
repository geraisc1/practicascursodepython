# TRATAMIENTO DE ERRORES
#try, exept, else,finally

try: #Esta funcion permite controlar el error de un programa al compilarlo
    numero1 = 3
    numero2 = 0
    divicion =  numero1 / numero2
    print(divicion)

except:#con esta funcion remplazamos el error de la terminal por un mensaje deseado
    print("Error en el codigo")

finally:#Este es el final del try con un respectivo mensaje
    print("El metodo try a terminado")

    

