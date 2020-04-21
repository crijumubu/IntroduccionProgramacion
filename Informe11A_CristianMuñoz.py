# -*- coding: utf-8 -*-

"Created on Mon Apr 20 16:25:50 2020"

def generador():
    import numpy as np
    ingresos=np.zeros(shape=(4,12))
    egresos=np.zeros(shape=(4,12))

    import random
    filas,columnas = ingresos.shape
    for i in range (0,filas):
        for i1 in range (0,columnas):
            numero_aleatorio_ingresos= random.randrange(100,180)
            numero_aleatorio_egresos= random.randrange(60,130)
            ingresos[i,i1]= numero_aleatorio_ingresos
            egresos[i,i1]= numero_aleatorio_egresos
    print(ingresos, egresos)

generador()

"@author: user"
