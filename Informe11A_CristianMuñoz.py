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
    return ingresos,egresos

def imprimir():
    ingresos,egresos= generador()
    meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    filas_in,columnas_in= ingresos.shape
    print("El arreglo ingresos tiene " + str(filas_in) + " filas y " + str(columnas_in) + " columnas")
    print(meses)
    print("Bucaramanga",ingresos[0]) 
    print("Floridablanca",ingresos[1]) 
    print("Girón",ingresos[2])
    print("Piedecuesta",ingresos[3])
    filas_e,columnas_e= egresos.shape
    print("El arreglo egresos tiene " + str(filas_e) + " filas y " + str(columnas_e) + " columnas")
    print(meses)
    print("Bucaramanga",egresos[0]) 
    print("Floridablanca",egresos[1]) 
    print("Girón",egresos[2])
    print("Piedecuesta",egresos[3])

imprimir()

"@author: user"
