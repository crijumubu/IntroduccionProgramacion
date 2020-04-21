# -*- coding: utf-8 -*-

"Created on Mon Apr 20 16:25:50 2020"

def generador(a,b):
    import numpy as np
    array=np.zeros(shape=(4,12))

    import random
    filas,columnas = array.shape
    for i in range (0,filas):
        for i1 in range (0,columnas):
            numero_aleatorio = random.randrange(a,b)
            array[i,i1]= numero_aleatorio
    print(array)

print("A continuación, ingrese el rango para los numeros pseudoaleatorios:")
a = int(input())
b= int(input())
generador(a,b)

"@author: user"



