# -*- coding: utf-8 -*-

"Created on Sun Apr 26 10:42:42 2020"

Presion_semanal=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,
                 119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,
                 118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,
                 106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,
                 108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,
                 122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,
                 110.67,107.73,105.76,107.85]

#Punto 1

long=len(Presion_semanal)
#Se inicializan variables como mayor y como menor con base en la lista
mayor=Presion_semanal[0]
menor=Presion_semanal[0]
#Se realiza un ciclo for el cual nos permitirá saber cual es el mayor y menor en la lista
for i in range(0,long):
    if mayor<Presion_semanal[i]:
        mayor=Presion_semanal[i]
    elif menor>Presion_semanal[i]:
        menor=Presion_semanal[i]
diferencia=round(mayor-menor,2)
#Se imprime la diferencia y se expresa en las unidades de medida correspondientes (KPa)
print("La diferencia entre la mayor y la menor presion promedio semanal registrada es " + str(diferencia) + "KPa")
    
#Punto 2

suma=0
#Se realiza un ciclo for el para calcular la suma de los datos 
for i in range(0,long):
    suma+=Presion_semanal[i]
#Se divide la suma entre el número datos y se halla la media
media_presion=round(suma/long,2)
#Se imprime la media con sus medidad respectivas
print("La media es: " + str(media_presion)+"KPa") 

#Se realiza una copia a la lista de la presión semanal ya que la tenemos que modificar estos datos y no queremos modificar la original
copia_presion_semanal=Presion_semanal.copy()
#Se crea la lista sin datos la cual irá a contener los datos ordenados
lista_ordenada=[]
#Se realiza un ciclo que va desde 0 hasta el número de datos de la lista
for i in range(0,long):
    #Se inicializa una variable como menor para con base en esta ir encontrado el menor
    menor=copia_presion_semanal[0]
    #Se realiza un ciclo que va desde 0 hasta el contador del ciclo anterior menos 1, el -1 se debe a que cada vez se hallará el menor y se eliminará este dato de la lista copia, por esto siempre irá una posición menos
    for i1 in range(0,long-i):
        if menor>copia_presion_semanal[i1]:
            menor=copia_presion_semanal[i1]
    #Una vez tengamos el menor de la lista, lo trasladaremos a la lista ordenada y lo eliminaremos de la lista copia
    copia_presion_semanal.remove(menor)
    lista_ordenada.append(menor)

#Se halla el número de datos de la lista ordenada    
long=len(lista_ordenada)
#Se realiza un condicional el cual nos hará saber que proceso tenemos que seguir para hallar la media
if long%2==0:
    #Se halla los dos datos intermedios y se promedian y con esto tenemos la mediana en caso de que la cantidad de datos de la lista ordenada sea par
    dato_intermedio=int(long/2)
    dato_intermedio_1=int(dato_intermedio-1)
    mediana= (lista_ordenada[dato_intermedio]+lista_ordenada[dato_intermedio_1])/2
else:
    #Se halla la mediana por medio de la división entera en caso qde que la cantidad de datos de la lista ordenada se impar
    mediana= lista_ordenada[long//2]
#Se imprime la mediana con las unidades correspondientes
print("La mediana es: " + str(mediana)+"KPa")

#Punto 4

#Se halla el número de datos de la lista inicial (la lista de las presiones)
long=len(Presion_semanal)
#Se inicializa la lista y se inicializa la sumas las cuales se irán sumando cada vez que hallen un número mayor a la media o un menor menor a la media
presion_mayor_menor_media=[]
suma_mayor=0
suma_menor=0
#Se realiza un ciclo for el cual va desde 0 hasta la cantidad de datos de la lista
for i in range(0,long):
    #Se realiza un condicional el cual me permitirá saber si la lista en la posición i es mayor o menor a la media y me ira sumando de a 1 
    if Presion_semanal[i]>media_presion:
        suma_mayor+=1
    else:
        suma_menor+=1
#Se ingresan las sumas a la lista anteriormente inicializada
presion_mayor_menor_media=[suma_mayor,suma_menor]
#Se imprime el resultados
print("La cantidad de semanas en las que la presión promedio semanal supera la media es " +str(presion_mayor_menor_media[0]))
print("La cantidad de semanas en las que la presión promedio semanal está por debajo la media es " +str(presion_mayor_menor_media[1]))

#Punto 6.1
 
#Se inicializa una lista y un contador con nombre de "semanas"  
temperatura_prom=[]
semana=1
#Se realiza un ciclo for el cual va desde 0 hasta la cantidad de datos de la lista inicial (La lista de presiones)
for i in range(0,long):
    #Con base en la formula se halla la temperatura
    temperatura=round((Presion_semanal[i]*510)/(17.16*0.082),2)
    #Se imprime el resultado y este se ingresa a la lista inicializada anteriormente, ademas se suma 1 al contador 
    print("La temperatura promedio para la semana " + str(semana) + " es: " + str(temperatura) + "K")
    temperatura_prom.append(temperatura)
    semana+=1

#Punto 6.2

#Se halla el número de datos de la lista creada en el punto anterior y se incializa una suma
long=len(temperatura_prom)
suma=0
#Se realiza un ciclo for para hallar la suma de todas las temperaturas
for i in range(0,long):
    suma+= temperatura_prom[i]
#Esta suma se divide sobre la cantidad de datos de la lista
media_temperatura=suma/long

#Se incializa una suma y se realiza un ciclo for
suma=0
for i in range(0,long):
    #Se halla la sumatoria de la varianza según la formula
    suma+=(temperatura_prom[i]-media_temperatura)**2
#Esta sumatoria se divide en la cantidad de datos de la lista
varianza=suma/long
#Se saca la raiz cuadrada de la varianza la cual me dará como resultado de la desviación estandar
desviacion_estandar=round(varianza**0.5,2)
#Se imprime la desviación estandar con sus unidades correspondientes(KPa)
print("La desviación estandar de las temperaturas promedio semanal es: " + str(desviacion_estandar)+"K")
    
#Punto 6.3  

#Se inicializan la lista que contendra las temperaturas mayores a la media y la lista que contendra las temperaturas menores a la media
temperatura_mayor=[]
temperatura_menor=[]
#Se realiza un ciclo desde 0 hasta la cantidad de datos de la lista de las temperaturas
for i in range(0,long):
    #Se crea un condicional el cual me permitirá saber cuando una temperatura es mayor o menor a la media y me la agrega a la lista correspondiente anteriormente creada
    if temperatura_prom[i]>media_temperatura:
        temperatura_mayor.append(temperatura_prom[i])
    else:  
        temperatura_menor.append(temperatura_prom[i])
#Se crea una lista con estas dos listas dentro
lista_de_lista_temp=[temperatura_mayor,temperatura_menor]   

#Punto 6.4

#Se realiza primero el procedimiento para las temperaturas mayores a la media
#Con la lista de listas creada anteriormente, la desfragmentamos y sacamos la lista la cual contiene las temperaturas mayores a la media
temperatura_mayor=lista_de_lista_temp[0]
#Se halla la cantidad de datos de la lista y se inicializa una suma
long_mayor=len(temperatura_mayor)
suma_mayor=0
#Se realiza un ciclo for para hallar la suma de las temperaturas
for i in range(0,long_mayor):
    suma_mayor+=temperatura_mayor[i]
#Esta suma se divide entre la cantidad de datos de la lista
media_mayor=suma_mayor/long_mayor

#Se inicializa otra suma y se realiza un ciclo dor el cual nos hallará la sumatoria según la formula de varianza para datos muestrales
suma_mayor=0
for i in range(0,long_mayor):
    suma_mayor+=(temperatura_mayor[i]-media_mayor)**2
#La suma la dividimos entre la cantidad de datos de la lista menos 1 y tendremos como resultado la varianza
varianza_mayor=suma_mayor/(long_mayor-1)
#Se halla la raiz cuadrada de la varianza y esto nos dará como resultado la desviación estandar
desviacion_estandar_mayor= round(varianza_mayor**0.5,2)
#Imprimimos y ponemos las unidades correspondientes
print("La desviación estandar para las temperaturas mayores a la media es: " + str(desviacion_estandar_mayor) +"K")

#Ahora se realiza el procedimiento para las temperaturas menores a la media
#Se realiza eactamente el mismo procedimiento anterior
temperatura_menor=lista_de_lista_temp[1]
long_menor=len(temperatura_menor)
suma_menor=0
for i in range(0,long_menor):
    suma_menor+=temperatura_menor[i]
media_menor=suma_menor/long_menor

suma_menor=0
for i in range(0,long_menor):
    suma_menor+=(temperatura_menor[i]-media_menor)**2
varianza_menor=suma_menor/(long_menor-1)
desviacion_estandar_menor= round(varianza_menor**0.5,2)
print("La desviación estandar para las temperaturas que no superan la media es: " + str(desviacion_estandar_menor) +"K")

#Punto 6.5

#Se promedian ambas desviaciones estandar halladas anteriormente
media_desviacion_mayor_menor=(desviacion_estandar_mayor+desviacion_estandar_menor)/2
#Se realiza la diferencia entre la desviación estandar del punto 6.2 y el resultado del promedio de las varianzas encontradas anteriormente
diferencia_desviaciones= round((desviacion_estandar)-(media_desviacion_mayor_menor),2)
#Se imprime esta diferencia con sus respectivas unidades
print("La diferencia entre la desviación estandar encontrada en el punto 6.2 y la desviación estandar encontrada en el punto anterior es: " +str(diferencia_desviaciones) +"KPa")
    
"author: user"