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

#%%Supercomputadora con mayor nucleos

def Supercomputadora_con_más_nucleos(Supercomputadoras):
    niveles,columnas= Supercomputadoras.shape
    máx= Supercomputadoras[0,1]
    nombre_máx_supercomputadora= Supercomputadoras[0,0]
    for i in range(1,niveles):
        if int(máx)<int(Supercomputadoras[i,1]):
            máx=Supercomputadoras[i,1]
            nombre_máx_supercomputadora= Supercomputadoras[i,0]
    print("La computadora que más tiene núcleos es " + nombre_máx_supercomputadora + " y tiene " + str(máx) + " núcleos")
    
Supercomputadora_con_más_nucleos(Supercomputadoras)

#%%SuperComputadoras que superen con su menor registro de TFlops/s el valor ingresado por el usuario 

def Supercomputadoras_Rmax(Supercomputadoras, a):
    niveles,columnas= Supercomputadoras.shape
    for i in range(0,niveles):
        if int(Supercomputadoras[i,2])>a:
            print("Las computadoras con mas de " +str(a) + " TFlops/s son: ")
                break
            else:
                print("No hay ninguna computadora con mas de " + str(a) + " TFlops/s")
                break
    
    for i in range(0,niveles):
        if int(Supercomputadoras[i,2])>a:
            print(Supercomputadoras[i,0])
        
a = int(input("Ingrese la cantidad de TFlops/s para determinar cuales supercomputadoras han tenido en su menor registro un valor mayor al ingresado: "))
Supercomputadoras_Rmax(Supercomputadoras, a)

#%%Promedio de cada una de las computadoras de su mínimo TFlops/s registrado y su máximo TFlops/s registrado 

def Supercomputadoras_promedio(Supercomputadoras):
    niveles,columnas= Supercomputadoras.shape
    suma=0
    cont=0
    for nivel in range(0,niveles):
        for columna in range(2, columnas):
            if columnas-1==columna:
                suma += int(Supercomputadoras[nivel,columna])
                cont += 1
                promedio= suma/cont
            else:
                suma += int(Supercomputadoras[nivel,columna])
                cont += 1
                
        print("El promedio de TFlops/s de la supercomputadora " + Supercomputadoras[nivel,0] + " es: " + str(round(promedio,2)))
        
Supercomputadoras_promedio(Supercomputadoras)         

"@author: user"
