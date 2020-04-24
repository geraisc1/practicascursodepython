"""
crear una funcion "pares" que devuelva un array de numeros pares entre 
dos valores pasados como parametros a la funcion (inicio y fin)

utilizar la funcion 'pares' con los numeros 1 y 30
utilizar la funcion 'pares' con los numeros 2 y 40
"""
import numpy as np 

def pares(inicio,fin):
    if (inicio % 2 == 0):
        array = np.arange(inicio,fin,2)
    else:
        inicio = inicio + 1
        array = np.arange(inicio,fin,2)
    return array

res = pares(1,30)
print(res)

res1 = pares(2,40)
print(res1)




