#Tratamiento de erroresII

try:
    num1 = 5
    num2 = 4
    num3 = 2


    resta = float(num2 - num3)
    print("El resultado de la resta es:  {}".format(resta))
    divcion = num1 / resta
    print("El resultado de la divicion es:  {}".format(divcion))
  
except:
    print("Error de codigo")
else:
    print("OPERACION CON EXITO!!!")
finally:
    print("try terminado")
    print("\n")


#Bloque2
try:
    num4 = 6
    num5 = 3
    num6 = 3

    resta2 = float(num5 - num6)
    print("El resultado de la divicion es: {}".format(resta2))

    divcion2 = (num4 / resta2)
    print("El resultado de la divicion es: {}".format(divcion2))

except ZeroDivisionError:
    print("ERROR EN LA OPERACION")
else:
    print("OPERACION CON EXITO!!!")

finally:
    print("Sentencia finalizada")





