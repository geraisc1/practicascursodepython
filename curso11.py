# operadores logicos (and, or, not)

numero1 = 4
numero2 = 5
numero3 = 20
numero4 = 12
 
menor = numero1 < numero2
print(menor)

mayor = numero3 > numero4
print(mayor)

#operador and necesita que los dos opciones sean verdaderas
operador = numero1 < numero2 and  numero3 > numero4
print(operador)

#operador or solo nececita que cualquiera de los dos se cumpla

operador = numero1 < numero2 or  numero4 > numero3

#operador not evalua lo contrario

operador = numero4 < numero2 
print(operador)

operador = not(numero4 < numero2 )
print(operador)

cadena = "hola como estas gera"
cadena = cadena.split()
print(cadena)

