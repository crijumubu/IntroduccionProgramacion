# -*- coding: utf-8 -*-
"Created on Thu Apr  2 16:10:55 2020"

import numpy as np

Utilidad = np.array ([27834*10**6,23789*10**6,30189*10**6,30967*10**6,32501*10**6,32701*10**6,31665*10**6,17155*10**6,4614*10**6,834*10**6])

#%% PUNTO 1

def diferencia1(Utilidad):
    
#Media de la utilidad operacional de los dos primeros años de registro

    suma1=0
    cont1=0
    for i1 in range(0,2):
        suma1 += Utilidad[i1]
        cont1 += 1
    media1 = suma1/cont1
<<<<<<< HEAD
   
=======

>>>>>>> 94c90b1904783e55f537ac7ca8a05bfd1483d3be
#Media de la utilidad operacional de los dos últimos años de registro

    suma2=0
    cont2=0
    for i2 in range(8,10):
        suma2 += Utilidad[i2]
        cont2 += 1
    media2 = suma2/cont2
    
#Diferencia de la media de utilidad operacional entre los dos ultimos años y los dos primeros años de registro

    diferencia2 = int(media1-media2)
    return diferencia2

print("La diferencia de la media en la utilidad operacional de Kellog's en los últimos dos años comparada con la de los primeros dos años de registro es " + str(diferencia1(Utilidad)) + " COP")

#%% PUNTO 2

def diferencia3(Utilidad):
    
#Año con mayor utilidad operacional

<<<<<<< HEAD
    long = len(Utilidad)
    mayor = Utilidad[0]
    cont3 = 0
    for i3 in range(1,long):
        if Utilidad[cont3]<Utilidad[i3]:
            mayor = Utilidad[i3]
        cont3 += 1

#Año con menor utilidad operacional

    menor = Utilidad[0]
    cont4 = 0
    for i4 in range(1,long):
        if Utilidad[cont4]>Utilidad[i4]:
            menor = Utilidad[i4]
        cont4 += 1
        
#Diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad

    diferencia4 =int(mayor-menor)
    return diferencia4

print("La diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad es " + str(diferencia3(Utilidad)) + " COP")

#%% PUNTO 3

def mediana(Utilidad):
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La mediana es: " + str(mediana) + " COP")
    
mediana(Utilidad)

#%% PUNTO 4

def media_mediana(Utilidad):
    
#Media
    
    long = len(Utilidad)
    suma3 = 0
    cont5 = 0
    for i5 in range(0,long):
        suma3 += Utilidad[i5]
        cont5 += 1
    media = int(suma3 / cont5)

#Mediana
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La media es: " + str(media) + " COP")
    print("La mediana es: " + str(mediana) + " COP")

media_mediana(Utilidad)

#%% PUNTO 5

def porcentaje_utilidad(Utilidad):
    
#Utilidad operacional acumulado
    
    long = len(Utilidad)
    suma4 = 0
    año = 2008
    for i6 in range(0,long):
        suma4 += Utilidad[i6]
        
#Utilidad operacional de cada año

    for i7 in range(0, long):
        porcentaje_que_aporta = round((Utilidad[i7] / suma4)*100 , 2)
        print("El porcentaje que le aporta la utilidad operacional del año " +str(año) + " es: " + str(porcentaje_que_aporta) + "%")
        año += 1
        
porcentaje_utilidad(Utilidad)
        




    
    
         
    
=======
>>>>>>> 94c90b1904783e55f537ac7ca8a05bfd1483d3be
"@author: user"
