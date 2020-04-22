# -*- coding: utf-8 -*-

"Created on Mon Apr 20 16:25:50 2020"

def generador():
    import numpy as np
    ingresos=np.zeros(shape=(4,12))
    egresos=np.zeros(shape=(4,12))

    import random
    filas_in,columnas_in= ingresos.shape
    for i in range (0,filas_in):
        for i1 in range (0,columnas_in):
            numero_aleatorio_ingresos= random.randrange(100,180)
            numero_aleatorio_egresos= random.randrange(60,130)
            ingresos[i,i1]= numero_aleatorio_ingresos
            egresos[i,i1]= numero_aleatorio_egresos
    print("Arreglo ingresos:")
    imprimir(ingresos)
    print("Arreglo egresos:")
    imprimir(egresos)
generador()

def imprimir(arreglo):
    meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    filas,columnas= arreglo.shape
    print("El arreglo tiene " + str(filas) + " filas y " + str(columnas) + " columnas")
    print(meses)
    print("Bucaramanga",arreglo[0]) 
    print("Floridablanca",arreglo[1]) 
    print("Girón",arreglo[2])
    print("Piedecuesta",arreglo[3])
