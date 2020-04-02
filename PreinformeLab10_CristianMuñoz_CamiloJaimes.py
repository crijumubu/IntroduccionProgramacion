# -*- coding: utf-8 -*-
"Created on Thu Apr  2 16:10:55 2020"

import numpy as np

Utilidad = np.array ([27834*10**6,23789*10**6,30189*10**6,30967*10**6,32501*10**6,32701*10**6,31665*10**6,17155*10**6,4614*10**6,834*10**6])

#Punto 1

def media(Utilidad):
    
#Media de la utilidad operacional de los dos primeros años de registro

    suma1=0
    cont1=0
    for i1 in range(0,2):
        suma1 += Utilidad[i1]
        cont1 += 1
    media1 = suma1/cont1
    return media1

#Media de la utilidad operacional de los dos últimos años de registro

    suma2=0
    cont2=0
    for i2 in range(8,10):
        suma2 += Utilidad[i2]
        cont2 += 1
    media2 = suma2/cont2
    
#Diferencia de la media de utilidad operacional entre los dos ultimos años y los dos primeros años de registro

    diferencia = abs(media1-media2)
    print(diferencia)
    
media(Utilidad)


   
        
        


"@author: user"



