# -*- coding: utf-8 -*-

"Created on Mon Apr 20 16:25:50 2020"

meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"]

def generador():
    #Se crea arreglos ingresos y egresos con el tamaño estipulado en la tabla
    import numpy as np
    ingresos=np.zeros(shape=(4,12))
    egresos=np.zeros(shape=(4,12))
    
    #Se crea los arreglos con números aleatorios por medio de la función random
    import random
    filas_in,columnas_in= ingresos.shape
    for i in range (0,filas_in):
        for i1 in range (0,columnas_in):
            numero_aleatorio_ingresos= random.randrange(100,180)
            numero_aleatorio_egresos= random.randrange(60,130)
            ingresos[i,i1]= numero_aleatorio_ingresos
            egresos[i,i1]= numero_aleatorio_egresos
    return ingresos,egresos

def imprimir(arreglo):
    #Se crea una lista con el nombre de las ciudades al inicio del algoritmo para mayor facilidad en la impresión
    filas,columnas= arreglo.shape
    print("El arreglo tiene " + str(filas) + " filas y " + str(columnas) + " columnas")
    print("Meses", meses)
    #Con el ciclo se imprime las ciudades y el arreglo
    for i in range(0,filas):
        print(ciudades[i],arreglo[i]) 

def restador(ingresos,egresos):
    import numpy as np
    #Se crea el arreglo ganancias con ceros y con el tamaño de la tabla
    ganancias=np.zeros(shape=(4,12))
    filas_in,columnas_in=ingresos.shape
    filas_egre,columnas_egre=egresos.shape
    #Si el arreglo ingresos tiene el mismo tamaño del arreglo egresos se realiza el ciclo y con la operación resta, cada valor que se encuentre de la resta se ingresará en el arreglo ganancias
    if filas_in==filas_egre and columnas_in==columnas_egre:
        for i in range(0,filas_in):
            for i1 in range(0, columnas_in):
                resta=ingresos[i,i1]-egresos[i,i1]
                ganancias[i,i1]=resta 
    return(ganancias)             

def mejor_ciudad(ganancias):
    filas,columnas=ganancias.shape
    suma_ganancias_bga=0
    #Se realiza la suma de las ganancias de cada uno de las ciudades por medio de los ciclos
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
    #Por medio de los condicionales sedetermina cual la ciudad con mayor ganancias y se imprime
    if suma_ganancias_flo<suma_ganancias_bga>suma_ganancias_gir and suma_ganancias_bga>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Bucaramanga")
    elif suma_ganancias_bga<suma_ganancias_flo>suma_ganancias_gir and suma_ganancias_flo>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Floridablanca")
    elif suma_ganancias_bga<suma_ganancias_gir>suma_ganancias_flo and suma_ganancias_gir>suma_ganancias_pie:
        print("La ciudad con mayor ganancias es Girón")
    else:
        print("La ciudad con mayor ganancias es Piedecuesta")

def peor_ciudad(ganancias):
    filas,columnas=ganancias.shape
    suma_ganancias_bga=0
    #Se realiza la suma de las ganancias de cada uno de las ciudades por medio de los ciclos
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
    #Por medio de los condicionales sedetermina cual la ciudad con menor ganancias y se imprime
    if suma_ganancias_flo>suma_ganancias_bga<suma_ganancias_gir and suma_ganancias_bga<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Bucaramanga")
    elif suma_ganancias_bga>suma_ganancias_flo<suma_ganancias_gir and suma_ganancias_flo<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Floridablanca")
    elif suma_ganancias_bga>suma_ganancias_gir<suma_ganancias_flo and suma_ganancias_gir<suma_ganancias_pie:
        print("La ciudad con menor ganancias es Girón")
    else:
        print("La ciudad con menor ganancias es Piedecuesta")
    return ganancias

def mejor_mes(ganancias):
    filas,columnas=ganancias.shape
    mejor_mes_bga=ganancias[0,0]
    #Se realizan un ciclo para cada ciudad para así determinar cual fue el mejor mes para cada ciudad
    #Ciclo para la ciudad de Bucaramanga
    for i in range(1,columnas):
        if mejor_mes_bga<ganancias[0,i]:
            mejor_mes_bga=ganancias[0,i]
            cont=i
        if columnas-1==i:
            print("El mejor mes en Bucaramanga fue: " +str(meses[cont]))
    mejor_mes_flo=ganancias[1,0]
    #Ciclo para la ciudad de Floridablanca
    for i1 in range(1,columnas):
        if mejor_mes_flo<ganancias[1,i1]:
            mejor_mes_flo=ganancias[1,i1]
            cont=i1
        if columnas-1==i1:
            print("El mejor mes en Floridablanca fue: " +str(meses[cont]))
    mejor_mes_gir=ganancias[2,0]
    #Ciclo para la ciudad de Girón
    for i2 in range(1,columnas):
        if mejor_mes_gir<ganancias[2,i2]:
            mejor_mes_gir=ganancias[2,i2]
            cont=i2
        if columnas-1==i2:
            print("El mejor mes en Girón fue: " +str(meses[cont]))
    mejor_mes_pie=ganancias[3,0]
    #Ciclo para la ciudad de Piedecuesta
    for i3 in range(1,columnas):
        if mejor_mes_pie<ganancias[3,i3]:
            mejor_mes_pie=ganancias[3,i2]
            cont=i3
        if columnas-1==i3:
            print("El mejor mes en Piedecuesta fue: " +str(meses[cont]))
        
def peor_mes(ganancias):
    filas,columnas=ganancias.shape
    peor_mes_bga=ganancias[0,0]
    #Se realizan un ciclo para cada ciudad para así determinar cual fue el peor mes para cada ciudad
    #Ciclo para la ciudad de Bucaramanga
    for i in range(1,columnas):
        if peor_mes_bga>ganancias[0,i]:
            peor_mes_bga=ganancias[0,i]
            cont=i
        if columnas-1==i:
            print("El peor mes en Bucaramanga fue: " +str(meses[cont]))
    peor_mes_flo=ganancias[1,0]
    #Ciclo para la ciudad de Floridablanca
    for i1 in range(1,columnas):
        if peor_mes_flo>ganancias[1,i1]:
            peor_mes_flo=ganancias[1,i1]
            cont=i1
        if columnas-1==i1:
            print("El peor mes en Floridablanca fue: " +str(meses[cont]))
    peor_mes_gir=ganancias[2,0]
    #Ciclo para la ciudad de Girón
    for i2 in range(1,columnas):
        if peor_mes_gir>ganancias[2,i2]:
            peor_mes_gir=ganancias[2,i2]
            cont=i2
        if columnas-1==i2:
            print("El peor mes en Girón fue: " +str(meses[cont]))
    peor_mes_pie=ganancias[3,0]
    #Ciclo para la ciudad de Piedecuesta
    for i3 in range(1,columnas):
        if peor_mes_pie>ganancias[3,i3]:
            peor_mes_pie=ganancias[3,i2]
            cont=i3
        if columnas-1==i3:
            print("El peor mes en Piedecuesta fue: " +str(meses[cont]))
    
def imprimir_personalizado(arreglo,mes_ini,mes_fin):
    filas,columnas=arreglo.shape
    #Se resta 1 al menos inicial y al mes final porque los arreglos y la lista meses empieza en 0 y no en 1
    mes_ini-=1
    mes_fin-=1
    cont_mes=mes_ini
    #Se realiza un cilo for que inicie en el mes inicial y termine en el mes final e imprima el ciclo solicitado en estos meses
    for i in range(mes_ini,mes_fin):
        print("\n","El arreglo en el mes " + str(meses[cont_mes]) + " es: ", end="")
        for i1 in range(0,filas):
            print(arreglo[i1,i],", ", end="")
            if filas-1==i1:
                print(arreglo[i1,i])
        cont_mes+=1
           
def promedio(ingresos,egresos,ganancias):
    filas_in,columnas_in=ingresos.shape
    filas_eg,columnas_eg=egresos.shape
    filas_ga,columnas_ga=ganancias.shape
    suma_in=0
    #Se realizan ciclos for en el cual se calcula la suma de los ingresos por cada ciudad y se divide en la cantidad de columnas y al final se imrpime el promedio, esto mismo se hace para los egresos y ganancias
    for i in range(0,filas_in):
        for i1 in range(0,columnas_in):
            suma_in+=ingresos[i,i1]
        promedio_in=round(suma_in/columnas_in,2)
        print("El promedio anual de ingresos en la ciudad de " + str(ciudades[i]) + " es: " + str(promedio_in))   
        suma_in=0
    suma_eg=0
    print("\n")
    for i in range(0,filas_eg):
        for i1 in range(0,columnas_eg):
            suma_eg+=egresos[i,i1]
        promedio_eg=round(suma_eg/columnas_eg,2)
        print("El promedio anual de egresos en la ciudad de " + str(ciudades[i]) + " es: " + str(promedio_eg))
        suma_eg=0
    suma_ga=0
    print("\n")
    for i in range(0,filas_ga):
        for i1 in range(0,columnas_ga):
            suma_ga+=ganancias[i,i1]
        promedio_ga=round(suma_ga/columnas_ga,2)
        print("El promedio anual de ganancias en la ciudad de " + str(ciudades[i]) + " es: " + str(promedio_ga))    
        suma_ga=0
        
def promedio_2(ingresos,egresos,ganancias):
    filas_in,columnas_in=ingresos.shape
    filas_eg,columnas_eg=egresos.shape
    filas_ga,columnas_ga=ganancias.shape
    
    #Arreglo ingresos
    #Se inicializan variables de mayor y menor del arreglo ingresos para cada ciudad
    mayor_bga_in=ingresos[0,0]
    menor_bga_in=ingresos[0,0]
    mayor_flo_in=ingresos[1,0]
    menor_flo_in=ingresos[1,0]
    mayor_gir_in=ingresos[2,0]
    menor_gir_in=ingresos[2,0]
    mayor_pie_in=ingresos[3,0]
    menor_pie_in=ingresos[3,0]
    #Se inicializan variables de suma del arreglo ingreso para cada ciudad
    suma_bga_in=0
    suma_flo_in=0
    suma_gir_in=0
    suma_pie_in=0
    #Se inicializa un ciclo el cual nos permite hallar el mayor y menor para cada ciudad
    for i in range(0,columnas_in):
        if mayor_bga_in<ingresos[0,i]:
            mayor_bga_in=ingresos[0,i]
        if menor_bga_in>ingresos[0,i]:
            menor_bga_in=ingresos[0,i]
        if mayor_flo_in<ingresos[1,i]:
            mayor_flo_in=ingresos[1,i]
        if menor_flo_in>ingresos[1,i]:
            menor_flo_in=ingresos[1,i]
        if mayor_gir_in<ingresos[2,i]:
            mayor_gir_in=ingresos[2,i]
        if menor_gir_in>ingresos[2,i]:
            menor_gir_in=ingresos[2,i]
        if mayor_pie_in<ingresos[3,i]:
            mayor_pie_in=ingresos[3,i]
        if menor_pie_in>ingresos[3,i]:
            menor_pie_in=ingresos[3,i]
    #Se realiza un ciclo con condicionales para así excluir el mayor y menor de la suma del arreglo para cada ciudad
    for i1 in range(0,columnas_in):
        if ingresos[0,i1]!=mayor_bga_in and ingresos[0,i1]!=menor_bga_in:
            suma_bga_in+=ingresos[0,i1]
        if ingresos[1,i1]!=mayor_flo_in and ingresos[1,i1]!=menor_flo_in:
            suma_flo_in+=ingresos[1,i1]
        if ingresos[2,i1]!=mayor_gir_in and ingresos[2,i1]!=menor_gir_in:
            suma_gir_in+=ingresos[2,i1]
        if ingresos[3,i1]!=mayor_pie_in and ingresos[3,i1]!=menor_pie_in:
            suma_pie_in+=ingresos[3,i1]
    #Con la suma hallado anteriormente se divide esta entra la cantidad de columnas y se imprime
    promedio_bga_in=round(suma_bga_in/(columnas_in-2))
    print("El promedio anual de ingresos en la ciudad de " + str(ciudades[0]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_bga_in))
    promedio_flo_in=round(suma_flo_in/(columnas_in-2),2)
    print("El promedio anual de ingresos en la ciudad de " + str(ciudades[1]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_flo_in))
    promedio_gir_in=round(suma_gir_in/(columnas_in-2),2)
    print("El promedio anual de ingresos en la ciudad de " + str(ciudades[2]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_gir_in))
    promedio_pie_in=round(suma_pie_in/(columnas_in-2),2)
    print("El promedio anual de ingresos en la ciudad de " + str(ciudades[3]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_pie_in))
    
    #Para el arreglo egresos y el arreglo ganancias se realiza el mismo procedimiento que con el arreglo ingresos
    #Arreglo egresos
    mayor_bga_eg=egresos[0,0]
    menor_bga_eg=egresos[0,0]
    mayor_flo_eg=egresos[1,0]
    menor_flo_eg=egresos[1,0]
    mayor_gir_eg=egresos[2,0]
    menor_gir_eg=egresos[2,0]
    mayor_pie_eg=egresos[3,0]
    menor_pie_eg=egresos[3,0]
    suma_bga_eg=0
    suma_flo_eg=0
    suma_gir_eg=0
    suma_pie_eg=0
    for i in range(0,columnas_eg):
        if mayor_bga_eg<egresos[0,i]:
            mayor_bga_eg=egresos[0,i]
        if menor_bga_eg>egresos[0,i]:
            menor_bga_eg=egresos[0,i]
        if mayor_flo_eg<egresos[1,i]:
            mayor_flo_eg=egresos[1,i]
        if menor_flo_eg>egresos[1,i]:
            menor_flo_eg=egresos[1,i]
        if mayor_gir_eg<egresos[2,i]:
            mayor_gir_eg=egresos[2,i]
        if menor_gir_eg>egresos[2,i]:
            menor_gir_eg=egresos[2,i]
        if mayor_pie_eg<egresos[3,i]:
            mayor_pie_eg=egresos[3,i]
        if menor_pie_eg>egresos[3,i]:
            menor_pie_eg=egresos[3,i]
    for i1 in range(0,columnas_eg):
        if egresos[0,i1]!=mayor_bga_eg and egresos[0,i1]!=menor_bga_eg:
            suma_bga_eg+=egresos[0,i1]
        if egresos[1,i1]!=mayor_flo_eg and egresos[1,i1]!=menor_flo_eg:
            suma_flo_eg+=egresos[1,i1]
        if egresos[2,i1]!=mayor_gir_eg and egresos[2,i1]!=menor_gir_eg:
            suma_gir_eg+=egresos[2,i1]
        if egresos[3,i1]!=mayor_pie_eg and egresos[3,i1]!=menor_pie_eg:
            suma_pie_eg+=egresos[3,i1]
    promedio_bga_eg=round(suma_bga_eg/(columnas_eg-2),2)
    print("El promedio anual de egresos en la ciudad de " + str(ciudades[0]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_bga_eg))
    promedio_flo_eg=round(suma_flo_eg/(columnas_eg-2),2)
    print("El promedio anual de egresos en la ciudad de " + str(ciudades[1]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_flo_eg))
    promedio_gir_eg=round(suma_gir_eg/(columnas_eg-2),2)
    print("El promedio anual de egresos en la ciudad de " + str(ciudades[2]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_gir_eg))
    promedio_pie_eg=round(suma_pie_eg/(columnas_eg-2),2)
    print("El promedio anual de egresos en la ciudad de " + str(ciudades[3]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_pie_eg))

    #Arreglos ganancias
    mayor_bga_ga=ganancias[0,0]
    menor_bga_ga=ganancias[0,0]
    mayor_flo_ga=ganancias[1,0]
    menor_flo_ga=ganancias[1,0]
    mayor_gir_ga=ganancias[2,0]
    menor_gir_ga=ganancias[2,0]
    mayor_pie_ga=ganancias[3,0]
    menor_pie_ga=ganancias[3,0]
    suma_bga_ga=0
    suma_flo_ga=0
    suma_gir_ga=0
    suma_pie_ga=0
    for i in range(0,columnas_ga):
        if mayor_bga_ga<ganancias[0,i]:
            mayor_bga_ga=ganancias[0,i]
        if menor_bga_ga>ganancias[0,i]:
            menor_bga_ga=ganancias[0,i]
        if mayor_flo_ga<ganancias[1,i]:
            mayor_flo_ga=ganancias[1,i]
        if menor_flo_ga>ganancias[1,i]:
            menor_flo_ga=ganancias[1,i]
        if mayor_gir_ga<ganancias[2,i]:
            mayor_gir_ga=ganancias[2,i]
        if menor_gir_ga>ganancias[2,i]:
            menor_gir_ga=ganancias[2,i]
        if mayor_pie_ga<ganancias[3,i]:
            mayor_pie_ga=ganancias[3,i]
        if menor_pie_ga>ganancias[3,i]:
            menor_pie_ga=ganancias[3,i]
    for i1 in range(0,columnas_ga):
        if ganancias[0,i1]!=mayor_bga_ga and ganancias[0,i1]!=menor_bga_ga:
            suma_bga_ga+=ganancias[0,i1]
        if ganancias[1,i1]!=mayor_flo_ga and ganancias[1,i1]!=menor_flo_ga:
            suma_flo_ga+=ganancias[1,i1]
        if ganancias[2,i1]!=mayor_gir_ga and ganancias[2,i1]!=menor_gir_ga:
            suma_gir_ga+=ganancias[2,i1]
        if ganancias[3,i1]!=mayor_pie_ga and ganancias[3,i1]!=menor_pie_ga:
            suma_pie_ga+=ganancias[3,i1]
    promedio_bga_ga=round(suma_bga_ga/(columnas_ga-2),2)
    print("El promedio anual de ganancias en la ciudad de " + str(ciudades[0]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_bga_ga))
    promedio_flo_ga=round(suma_flo_ga/(columnas_ga-2),2)
    print("El promedio anual de ganancias en la ciudad de " + str(ciudades[1]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_flo_ga))
    promedio_gir_ga=round(suma_gir_ga/(columnas_ga-2),2)
    print("El promedio anual de ganancias en la ciudad de " + str(ciudades[2]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_gir_ga))
    promedio_pie_ga=round(suma_pie_ga/(columnas_ga-2),2)
    print("El promedio anual de ganancias en la ciudad de " + str(ciudades[3]) + " excluyendo el valor mas alto y mas bajo es: " + str(promedio_pie_ga))

def extraer_proporciones(ganancias):
    filas_ga,columnas_ga=ganancias.shape
    #Se inicializan contadores para los valores positivos y para los valores negativos
    cont_po=0
    cont_ne=0
    #Se realiza un ciclo for para determinar cuantos valores fueron postivos y cuantos negativos
    for i in range(0,filas_ga):
        for i1 in range(0,columnas_ga):
            if ganancias[i,i1]>0:
                cont_po+=1
            else:
                cont_ne+=1
        #Se calcula el porcentaje por medio del contador y se divide entre el número de columnas, este resultado se multiplica por 100 para calcular el porcentaje y se imprime
        por_ga_po=round((cont_po/columnas_ga)*100,2)
        por_ga_ne=round((cont_ne/columnas_ga)*100,2)
        print("El porcentaje de meses en los que se generaron ganancias en la ciudad de " +str(ciudades[i]) +" es: " +str(por_ga_po)+"%")
        print("El porcentaje de meses en los que se generaron pérdidas en la ciudad de " +str(ciudades[i]) +" es: " +str(por_ga_ne) +"%")                         

def generador3D(ingresos,egresos):
    filas_in,columnas_in=ingresos.shape
    filas_eg,columnas_eg=egresos.shape
    import numpy as np
    #Se crean arreglos de ingresos y egresos para cada año y con base en el arreglo ingresos y egresos y la información dada se calculan los demás, es decir, los ingresos y egresos de los años anteriores
    ingresos_2018=np.zeros(shape=(filas_in,columnas_in))
    egresos_2018=np.zeros(shape=(filas_eg,columnas_eg))
    ingresos_2018=(ingresos)*(1-(9.5/100))
    egresos_2018=(egresos)*(1-(5.6/100))
    
    ingresos_2017=np.zeros(shape=(filas_in,columnas_in))
    egresos_2017=np.zeros(shape=(filas_eg,columnas_eg))
    ingresos_2017=(ingresos_2018)*(1-(9.5/100))
    egresos_2017=(egresos_2018)*(1-(5.6/100))
    
    ingresos_2016=np.zeros(shape=(filas_in,columnas_in))
    egresos_2016=np.zeros(shape=(filas_eg,columnas_eg))
    ingresos_2016=(ingresos_2017)*(1-(9.5/100))
    egresos_2016=(egresos_2017)*(1-(5.6/100))

    ingresos_2015=np.zeros(shape=(filas_in,columnas_in))
    egresos_2015=np.zeros(shape=(filas_eg,columnas_eg))
    ingresos_2015=(ingresos_2016)*(1-(9.5/100))
    egresos_2015=(egresos_2016)*(1-(5.6/100))
    
    #Se crean los arreglo ingresos y egresos 3D con base en los arreglos anteriormente hallados
    ingresos3D=np.array([[ingresos_2015],[ingresos_2016],[ingresos_2017],[ingresos_2018],[ingresos]])
    egresos3D=np.array([[egresos_2015],[egresos_2016],[egresos_2017],[egresos_2018],[egresos]])
    return ingresos3D,egresos3D
 
def imprimir3D(arreglo):
    #Se convierte el arreglo ingresado a unidimensional para mayor facilidad
    arreglo3D=arreglo.ravel()
    cont_ciudades=0
    año=2015
    cont=0
    print("Año " +str(año),"\n")
    print(meses)
    print(ciudades[cont_ciudades],": ",end="")
    #Se crea un ciclo for el cual me permitirá iterar el el arreglo convertido a unidimensional
    for i in range(0,5):
        for i1 in range(0,len(ciudades)*len(meses)):
            #Se crea una condición para que cuando i llegue a un múltiplo de los meses, es decir 12,24,etc, me deje de imprimir los datos para la ciudad que me los estaba imprimiendo, y pasa a la siguiente ciudad 
            if i1==len(meses) or i1==(len(meses)*2) or i1==(len(meses)*3):
                cont_ciudades+=1
                print("\n")
                print(ciudades[cont_ciudades],": ",end="")
            #Se crea un condicional mas que todo para dar un poco mas de estética a la tabla, cuando i esté en la última vuelta para llegar a un múltiplo de los meses me imprima el dato sin una coma al final, esto para evitar que me quede la coma al final como se dice volando
            if i1==((len(meses)*1)-1) or i1==((len(meses)*2)-1) or i1==((len(meses)*3)-1) or i1==((len(meses)*4)-1):
                print(arreglo3D[cont])
            else:
                print(arreglo3D[cont],", ",end="")
            cont+=1
        cont_ciudades=0
        año+=1
        #Se crea una condición para que cuando el año sea 2020,es decir ya se vaya a acabr el ciclo, no me imprima nada el año, ni la ciudad para la siguiente iteración ya que pues, ya no habrá mas iteraciones
        if año!=2020:
            print("\n")
            print("Año " +str(año),"\n")
            print(meses)
            print(ciudades[cont_ciudades],": ",end="")                

def calcular_ganancias3D(arreglo_1_3D,arreglo_2_3D):
    import numpy as np
    #Se crea un tercer arreglo que se copia de un arreglo ingresado, para así tener las especificaciones de tamaño y demás, los valores que tiene no me servirán y mas adelante serán reemplazados
    arreglo_3_3D=np.array([arreglo_1_3D])
    #Se convierten los arreglos a unidimensionales para mayor facilidad
    ingresos3D=arreglo_1_3D.ravel()
    egresos3D=arreglo_2_3D.ravel()
    ganancias3D=arreglo_3_3D.ravel()
    #Se crea la variable tamaño para determinar cuantos datos hay en el arreglo
    tamaño=ganancias3D.size
    #Se crea un ciclo que me reste los ingresos y egresos y me los guarde en el arreglo ganancias3D
    for i in range(0,tamaño):
        ganancias3D[i]=ingresos3D[i]-egresos3D[i]
    return ganancias3D
    
print("Arreglo ingresos:")
ingresos,egresos=generador()
imprimir(ingresos)
print("Arreglo egresos:")
imprimir(egresos)
print("Arreglo ganacias:")
ganancias=restador(ingresos,egresos)
imprimir(ganancias)
mejor_ciudad(ganancias)
peor_ciudad(ganancias)
mejor_mes(ganancias)
peor_mes(ganancias)
arreglo=input("Ingreso el nombre del arreglo, ya sea ingresos, egresos o ganancias: ")
if arreglo=="ingresos":
    arreglo=ingresos
elif arreglo=="egresos":
    arreglo=egresos
else:
    arreglo=ganancias
mes_ini=int(input("Ingrese el mes de inicio: "))
mes_fin=int(input("Ingrese el mes de fin: "))
imprimir_personalizado(arreglo,mes_ini,mes_fin)
promedio(ingresos,egresos,ganancias)
promedio_2(ingresos,egresos,ganancias)
extraer_proporciones(ganancias)
ingresos3D,egresos3D=generador3D(ingresos,egresos)
ganancias3D=calcular_ganancias3D(ingresos3D,egresos3D)
print("\n","INGRESOS:","\n")
imprimir3D(ingresos3D)
print("\n","EGRESOS:","\n")
imprimir3D(egresos3D)
print("\n","GANANCIAS:","\n")
imprimir3D(ganancias3D)

"@author: user"
