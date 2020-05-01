# -*- coding: utf-8 -*-

"Created on Thu Apr 16 12:28:46 2020"

import numpy as np

Supercomputadoras = np.array([
    ['Summit' , '2414592' , '148600' , '200794'],
    ['Sierra' , '1572480' , '94640' , '125712'],
    ['Sunway TaihuLight' , '10649600' , '93014' , '125435'],
    ['Tianhe-2A' , '4981760' , '61444' , '100678'],
    ['Frontera' , '448448' , '23516' , '38745'],
    ['Piz Daint' , '387872' , '21230' , '27154'],
    ['Trinity' , '979072' , '20158' , '41461'],
    ['AI Bridging Cloud Infrastructure (ABCI)' , '391680' , '19880' , '32576'],
    ['SuperMUC-NG' , '305856' , '19476' , '26873'],
    ['Lasen' , '288288' , '18200' , '23047']])

#Lista de listas de las supercomputadoras según su promedio de los valores asignados, imprimir la supercomputadora con su respectivo promedio

#Se inicializa una lista la cual contendrá las listas de cada una de las supercomputadoras con su respectivo promedio
lista_promedio=[]
#Se crea las variables filas y columnas las cuales contendrá el tamaño del arreglo bidimensional inicializado
filas,columnas=Supercomputadoras.shape
#Se crea un ciclo for de 0 hasta la cantidad de filas y dentro de este se inicializa variables
for i in range(0,filas):
    promedio=0
    suma=0
    cont=0
    #Se crea un ciclo for de 1 hasta la cantidad de columnas, no se toma en cuenta la columna 0 ya que esta contiene el nombre de las supercomputadoras 
    for i1 in range(1,columnas):
        #Se crea la variable suma la cual irá sumando los valores y por medio de la variable 'cont' me permitirá saber cuantos datos sumé para poderlo dividir en esta cantidad y así hallar el promedio
        suma+=int(Supercomputadoras[i][i1])
        cont+=1
    #Se calcula el promedio
    promedio=round(suma/cont,2)
    #Se crea una 'lista_variable' la cual contendrá el nombre de la supercomputadora y el promedio calculado anteriormente
    lista_variable=[Supercomputadoras[i][0],promedio]
    #Por medio de la lista variable hecha anteriormente se agrega a la 'lista_promedio' inicializada al inicio del problema
    lista_promedio.append(lista_variable)
#Se imprime la lista de listas para verificar el resultado
print("Lista de las supercomputadoras según su promedio de los valores asignados: ",lista_promedio,"\n")

#Crear un diccionario el cual contenga las supercomputadoras con su máximo de T/Flops y el usuario pueda modificar el máximo de T/Flops de la supercomputadora que él desee, puede hacerlo las veces que quiera y los cambios serán guardados

#Se inicializa un contador
cont=0
#Se crea un ciclo for el cual me permitirá imprimir una especie de tabla, la cual tiene un número y al frente la supercomputadora correspondiente
for i in range(0,filas):
    print(cont,' -> ',Supercomputadoras[i][0])
    cont+=1
#Se inicializan variables
long=len(lista_promedio)
c=1
#Se realiza un ciclo while el cual me permitirá hacer el procedimiento indeterminadas veces
while c!=0:
    a=int(input("Ingrese el número correspondiente para la supercomputadora que usted desee modificar sus T/Flops: "))
    b=int(input("Ingrese la cantidad máxima de T/Flops que desea agregarle la supercomputadora: "))
    #Se realiza un condicional el cual me permitirá saber si va en la primera iteración del ciclo while, esto con el fin de que me haga todo el proceso para la creación del diccionario en la primera iteración para después no tener que volverlo a realizar
    if c==1:
        #Se inicializa el diccionario
        Supercomputadoras_TFlops={}
        #Se realiza un ciclo for y dentro de este un condicional el cual me permitirá asignarle los valores correspondientes al diccionario
        for i in range(0,long):
            if a!=i:
                Supercomputadoras_TFlops[Supercomputadoras[i][0]]=Supercomputadoras[i][3]
            else:
                Supercomputadoras_TFlops[Supercomputadoras[i][0]]=b
    else:
        #Se realiza un ciclo for y dentro de este un condicional el cual me permitirá asignarle el valor ingresado por el usurio a la supercomputadora correspondiente y una vez que lo asignado se saldrá del ciclo
        for i in range(0,long):
            if a==i:
                Supercomputadoras_TFlops[Supercomputadoras[i][0]]=b
                break
    c=int(input("Si desea ingresar otra modificación ingrese un número diferente de cero: "))
    #Se realiza un condicional el cual me permitirá imprimir cierto mensaje dependiendo la condición y me imprimirá el diccionario
    if c!=0:
        print("Hasta el momento así va el diccionario: ",Supercomputadoras_TFlops)
    else:
        print("El diccionario quedó así: ",Supercomputadoras_TFlops,"\n")

#Con base en el primer punto halle la desviación estandar para cada supercomputadora

#Se inicializa variable
long=len(lista_promedio)
#Se realiza un ciclo for de 0 hasta la longitud de la lista realizada en el primer punto
for i in range(0,long):
    #Se inicializa la variable suma y se realiza un ciclo for de 1 hasta la cantidad de columnas, se inicia en 1 porque en 0 se encuentra el nombre de la supercomputadora
    sumatoria=0
    for i1 in range(1,columnas):
        sumatoria+=(lista_promedio[i][1]-int(Supercomputadoras[i][i1]))**2
    #Se divide la sumatoria y se divide en la cantidad de columnas -2 y hallamos la varianza, -2 porque de todas las columnas tomamos una menos y como es desviación estandar muestral ya que no tomamos en cuenta todos los valores de donde sacamos la información tenemos que restarle 1
    varianza=(sumatoria)/(columnas-2)
    #Se saca la raiz cuadrada de la varianza y encontramos la desviación estandar
    desviación_estandar=round(varianza**0.5,2)
    print("La desviación estandar de los valores de la supercomputadora",Supercomputadoras[i][0], "es: ", desviación_estandar)
    
"@author: user" 
