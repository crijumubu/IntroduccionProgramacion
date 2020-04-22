# -*- coding: utf-8 -*-

"Created on Mon Apr 20 16:25:50 2020"

meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

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
    return ingresos,egresos

def imprimir(arreglo):
    filas,columnas= arreglo.shape
    print("El arreglo tiene " + str(filas) + " filas y " + str(columnas) + " columnas")
    print(meses)
    print("Bucaramanga",arreglo[0]) 
    print("Floridablanca",arreglo[1]) 
    print("Girón",arreglo[2])
    print("Piedecuesta",arreglo[3])

def restador():
    import numpy as np
    ganancias=np.zeros(shape=(4,12))
    ingresos,egresos= generador()
    filas_in,columnas_in=ingresos.shape
    filas_egre,columnas_egre=ingresos.shape
    if filas_in==filas_egre and columnas_in==columnas_egre:
        for i in range(0,filas_in):
            for i1 in range(0, columnas_in):
                resta=ingresos[i,i1]-egresos[i,i1]
                ganancias[i,i1]=resta
    print("Arreglo ganacias:")
    imprimir(ganancias) 
    return(ganancias)             
       
def mejor_ciudad():
    ganancias= restador()
    filas,columnas=ganancias.shape
    suma_ganancias_bga=0
    for i in range(0,columnas):
        suma_ganancias_bga+=ganancias[0,i]
    suma_ganancias_flo=0
    for i in range(0,columnas):
        suma_ganancias_flo+=ganancias[1,i] 
    suma_ganancias_gir=0
    for i in range(0,columnas):
        suma_ganancias_gir+=ganancias[2,i]
    suma_ganancias_pie=0
    for i in range(0,columnas):
        suma_ganancias_pie+=ganancias[3,i]
    if suma_ganancias_flo<suma_ganancias_bga>suma_ganancias_gir and suma_ganancias_bga>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Bucaramanga")
    elif suma_ganancias_bga<suma_ganancias_flo>suma_ganancias_gir and suma_ganancias_flo>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Floridablanca")
    elif suma_ganancias_bga<suma_ganancias_gir>suma_ganancias_flo and suma_ganancias_gir>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Girón")
    else:
        print("La ciudad con mayor ganancias es Piedecuesta")
    return ganancias

def peor_ciudad():
    ganancias= mejor_ciudad()
    filas,columnas=ganancias.shape
    suma_ganancias_bga=0
    for i in range(0,columnas):
        suma_ganancias_bga+=ganancias[0,i]
    suma_ganancias_flo=0
    for i in range(0,columnas):
        suma_ganancias_flo+=ganancias[1,i] 
    suma_ganancias_gir=0
    for i in range(0,columnas):
        suma_ganancias_gir+=ganancias[2,i]
    suma_ganancias_pie=0
    for i in range(0,columnas):
        suma_ganancias_pie+=ganancias[3,i]
    if suma_ganancias_flo>suma_ganancias_bga<suma_ganancias_gir and suma_ganancias_bga<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Bucaramanga")
    elif suma_ganancias_bga>suma_ganancias_flo<suma_ganancias_gir and suma_ganancias_flo<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Floridablanca")
    elif suma_ganancias_bga>suma_ganancias_gir<suma_ganancias_flo and suma_ganancias_gir<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Girón")
    else:
        print("La ciudad con menor ganancias es Piedecuesta")
    return ganancias

def mejor_mes():
    ganancias=peor_ciudad()
    filas,columnas=ganancias.shape
    mejor_mes_bga=ganancias[0,0]
    for i in range(1,columnas):
        if mejor_mes_bga<ganancias[0,i]:
            mejor_mes_bga=ganancias[0,i]
            cont=i
        if columnas-1==i:
            print("El mejor mes en Bucaramanga fue: " +str(meses[cont]))
    mejor_mes_flo=ganancias[1,0]
    for i1 in range(1,columnas):
        if mejor_mes_flo<ganancias[1,i1]:
            mejor_mes_flo=ganancias[1,i1]
            cont=i1
        if columnas-1==i1:
            print("El mejor mes en Floridablanca fue: " +str(meses[cont]))
    mejor_mes_gir=ganancias[2,0]
    for i2 in range(1,columnas):
        if mejor_mes_gir<ganancias[2,i2]:
            mejor_mes_gir=ganancias[2,i2]
            cont=i2
        if columnas-1==i2:
            print("El mejor mes en Girón fue: " +str(meses[cont]))
    mejor_mes_pie=ganancias[3,0]
    for i3 in range(1,columnas):
        if mejor_mes_pie<ganancias[3,i3]:
            mejor_mes_pie=ganancias[3,i2]
            cont=i3
        if columnas-1==i3:
            print("El mejor mes en Piedecuesta fue: " +str(meses[cont]))
    
mejor_mes() 
        
"@author: user"
