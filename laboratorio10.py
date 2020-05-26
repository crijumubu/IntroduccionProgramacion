"Created on Tue Apr  7 16:52:49 2020"

def a_power_b(numeros_a,numeros_b):
    cont = 0
    par = 0
    impar = 0   
    total = 1
    long= len(numeros_b)
#Se realiza un ciclo for dependiendo la cantidad de números ingresados
    for i in range(0, long):
        c = numeros_a[i]
        d = int(numeros_b[i]+1)
#Se realiza un ciclo for para realizar las potencias que se ingresaron
        for i1 in range(1,d):
            total *= c
#Se inicializa un contador el cual nos permitira saber cual fue la potencia que se realizó
            cont1 = i
        print("El resultado de la potencia del par de números " + str(cont1) + " es: " +str(int(total)))
#Se inicializa otro contador el cual nos permitirá saber cuantas potencias se realizaron
        cont += 1
#Se realiza un condicional para saber si el resultado de la potencia que se resalizó es par o impar 
        if total%2==0:
            par += 1
        else:
            impar += 1
        total = 1
    print("Se calcularon " + str(cont) + " potencias" + " , " + str(par) + " veces el resultado de la potencia fue par y " + str(impar) + " veces el resultado de la potencia fue impar")

def mean_arreglo(numeros_a,numeros_b):
#Se inicializa el arreglo en el cual se guardará el promedio de los valores
    promedio=[]
    long_a= len(numeros_a)
    suma_a=0
    cont_a=0
#Se realiza un ciclo for para calcular el promedio de los valores de a, es decir, los valores que se ingresaron como base
    for i in range(long_a):
        suma_a += numeros_a[i]
        cont_a += 1
#Se realiza una lista la cual tendrá el valor promedio de los valores a, es decir los valores que se ingresaron como base
    numeros_a=[]
    promedioa = suma_a/cont_a
    numeros_a.append(round(promedioa,0))
  
    long_b= len(numeros_b)
    suma_b=0
    cont_b=0
#Se realiza un ciclo for para calcular el promedio de los valores de b, es decir, los valores que se ingresaron como exponente
    for i1 in range(long_b):
        suma_b += numeros_b[i1]
        cont_b += 1
#Se realiza una lista la cual tendrá el valor promedio de los valores b, es decir los valores que se ingresaron como exponente
    numeros_b=[]
    promediob = suma_b/cont_b
    numeros_b.append(round(promediob,0))

#Se invoca la función a_power_b para calcular la potencia promedio de a y la potencia promedio de b  
    a_power_b(numeros_a,numeros_b)

#se suma el promedio de a y el promedio de b y lo dividimos en dos, para así obtener el promedio total
    promedio_total= (promedioa+promediob)/2
    promedio.append(promedio_total)
    return promedio

def std_arreglo(numeros_a,numeros_b):
    long_a= len(numeros_a)
    numerador_a=0
    suma_a=0
    cont_a=0
#Se halla la media o promedio de los valores de a, ingresados como bases
    for i in range(long_a):
        suma_a += numeros_a[i]
        cont_a += 1
    promedioa = suma_a/cont_a
#Se halla la varinza de los valores de a, ingresados como bases
    for i in range(0,long_a):
        operacion_a= round((numeros_a[i]-promedioa)**2,2)
        numerador_a += operacion_a
    varianza_al_cuadrado_numeros_a= numerador_a/long_a
#Con base en la varianza de a, hallamos la desviación de los valores de a, ingresados como bases
    desviacion_numeros_a= round((varianza_al_cuadrado_numeros_a)**0.5,2)
    print("La desviacion estandar de los valores ingresados como a, es decir de los valores ingresados como bases es: " + str(desviacion_numeros_a))

    long_b= len(numeros_b)
    suma_b=0
    cont_b=0
    numerador_b=0
#Se halla la media o promedio de los valores de b, ingresados como exponentes
    for i1 in range(long_b):
        suma_b += numeros_b[i1]
        cont_b += 1
    promediob = suma_b/cont_b
#Se halla la varinza de los valores de b, ingresados como exponentes  
    for i1 in range(0,long_b):
        operacion_b=round((numeros_a[i1]-promediob)**2,2)
        numerador_b += operacion_b   
    varianza_al_cuadrado_numeros_b= numerador_b/long_b
#Con base en la varianza de b, hallamos la desviación de los valores de b, ingresados como exponentes
    desviacion_numeros_b= round((varianza_al_cuadrado_numeros_b)**0.5,2)
    print("La desviacion estandar de los valores ingresados como a, es decir de los valores ingresados como bases es: " + str(desviacion_numeros_b))

#Con base en la varinza de a y la varianza de b, hallamos la varianza total que es la media de estos dos
    varianza_total_al_cuadrado= ((varianza_al_cuadrado_numeros_a + varianza_al_cuadrado_numeros_b)/2)
    desviacion_total= round((varianza_total_al_cuadrado)**0.5,2)
    print("La desviación estandar de todos los valores ingresados es: " +str(desviacion_total))

def norm_arreglo(numeros_a,numeros_b):
    long_a= len(numeros_a)
    numerador_a=0
    suma_a=0
    cont_a=0
#Se halla la media o promedio de los valores de a, ingresados como bases
    for i in range(long_a):
        suma_a += numeros_a[i]
        cont_a += 1
    promedioa = suma_a/cont_a
#Se halla la varinza de los valores de a, ingresados como bases
    for i in range(0,long_a):
        operacion_a= round((numeros_a[i]-promedioa)**2,2)
        numerador_a += operacion_a
    varianza_al_cuadrado_numeros_a= numerador_a/long_a
    desviacion_estandar_a= (varianza_al_cuadrado_numeros_a)**0.5
#Se halla la estandarización de los valores de a
    estandarizacion_a=0
    for i in range(long_a):
        operacion_a= (numeros_a[i]-promedioa)/desviacion_estandar_a
        estandarizacion_a += operacion_a
    print("La estandarización de los valores ingresados como a es: " +str(estandarizacion_a))
    
    long_b= len(numeros_b)
    suma_b=0
    cont_b=0
    numerador_b=0
#Se halla la media o promedio de los valores de b, ingresados como exponentes
    for i1 in range(long_b):
        suma_b += numeros_b[i1]
        cont_b += 1
    promediob = suma_b/cont_b
#Se halla la varinza de los valores de b, ingresados como exponentes  
    for i1 in range(0,long_b):
        operacion_b=round((numeros_a[i1]-promediob)**2,2)
        numerador_b += operacion_b   
    varianza_al_cuadrado_numeros_b= numerador_b/long_b
    desviacion_estandar_b= (varianza_al_cuadrado_numeros_b)**0.5
#Se halla la estandarización de los valores de b
    estandarizacion_b=0
    for i in range(long_b):
        operacion_b= (numeros_b[i]-promediob)/desviacion_estandar_b
        estandarizacion_b += operacion_b
    print("La estandarización de los valores ingresados como b es: " +str(estandarizacion_b))
#Una vez obtenida la estandarización de a y de b, hallamos la estandarizacion total
    estandarizacion_total= round((estandarizacion_a+estandarizacion_b)/2,2)
    print("La estandarización de todos los valores ingresados: " +str(estandarizacion_total))

#Hallamos el nuevo valor promedio, teniendo en cuenta nuestros nuevos valores, que son la estandarizacion de a y de b
    nuevo_promedio= (estandarizacion_a+estandarizacion_b)/2
    print("El nuevo promedio de los valores ya estandarizados es: " +str(nuevo_promedio))
#Hallamos la nueva varianza, teniendo en cuenta nuestros nuevos valores, y con ella la nueva desviación estandar
    nueva_varinza_total_al_cuadrado= ((estandarizacion_a-nuevo_promedio)**2)+((estandarizacion_b-nuevo_promedio)**2)/2
    nueva_desviacion_total= nueva_varinza_total_al_cuadrado**0.5
    print("La nueva desviación estandar es: " + str(nueva_desviacion_total))

numeros_a=[]
numeros_b=[]
n = int(input("¿Cuantos parejas de números quiere ingresar? "))
for i in range(n):
    numeroa= int(input("Ingrese un número que será la base de la potencia: "))
    numeros_a.append(numeroa)
    numerob= int(input("Ingrese un número que será el exponente de las base: "))
    numeros_b.append(numerob)
a_power_b(numeros_a,numeros_b)
print("El promedio de los valores ingresados es: " +str(mean_arreglo(numeros_a,numeros_b)))
std_arreglo(numeros_a,numeros_b)
norm_arreglo(numeros_a,numeros_b)

"@author: user"