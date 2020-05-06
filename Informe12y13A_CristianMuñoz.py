# -*- coding: utf-8 -*-

"Created on Mon May  4 10:41:45 2020"

cartas = ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" ,
"Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" ,
"Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" ,
"Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers",
"Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" ,
"Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" ,
"Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" ,
"Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" ,
"Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" ,
"Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" ,
"Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" ,
"Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat",
"Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns",
"Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons",
"Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" ,
"Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" ,
"Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]

premium =["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

#Punto 1 y 2

def Imprimir(lista):
    #Por medio de la función len se halla la cantidad de elementos y se imprime junto a la lista
    print("La lista tiene " + str(len(lista)) + " elementos")
    print(lista)


#Punto 3 y 4

def Generador(lista,cantidad_elementos):
    #Se crea una lista copia de la lista ingresada para poderla modificar
    lista_copia=lista.copy()
    #Se crea un condicional el cual me permitirá evaluar si la cantidad de elementos de la lista es mayor o menor a la cantidad de elementos ingresada
    if len(lista)>=cantidad_elementos:
        import random
        #Se crea una lista de nombre 'lista_final' la cual está vacia y se le irá agregando elementos mientras se va realizando el proceso
        lista_terminada=[]
        #Se realiza un ciclo for desde 0 hasta la cantidad de elementos solicitados
        for i in range(0,cantidad_elementos):
            #Por medio de la función random se crea un número aleatorio en el rango de 0 hasta la cantidad de elementos de la lista
            numero_aleatorio=random.randint(0,len(lista_copia))
            #Se accede al elemento en la posición del número aleatorio encontrado y se almacena en una variable
            elemento_aleatorio=lista_copia[numero_aleatorio]
            #Se agrega la variable anterior a la lista de nombre 'lista_terminada'
            lista_terminada.append(elemento_aleatorio)
            #Se elimina este elemento de la lista copia, con el fin de que no se vaya a repetir
            lista_copia.remove(lista_copia[numero_aleatorio])
        #Se retorna la lista de nombre 'lista_terminada'
        return(lista_terminada)
    
    else:
        #Se le dice al usuario que la cantidad de elementos ingresada es mayor a los elementos de la lista en caso de que así lo sea
        print("La cantidad ingresada de elementos sobrepasa la cantidad de elementos de la lista")

#Punto 5 y 6

def Combinador(lista_A,lista_B):
    #Se halla la cantidad de elementos de las listas ingresadas
    long_A=len(lista_A)
    long_B=len(lista_B)
    #Se crea un condicional el cual me permitirá saber cual el la lista con mayor y menor cantidad de elementos
    if long_A>long_B:
        mayor=long_A
        lista_mayor=lista_A
        menor=long_B
        lista_menor=lista_B
    else:
        mayor=long_B
        lista_mayor=lista_B
        menor=long_A
        lista_menor=lista_A 
    #Se crea una lista vacía la cual contendra los números aleatorios los cuales irán desde 0 hasta la cantidad de elementos de la lista mayor menos 1, esto debido a que al hacer el procedimiento me toma en cuenta este valor, y este valor no existe en la lista por lo que se saldría de rango
    lista_numeros_aleatorios=[]
    #Se realiza un ciclo for desde 0 hasta la cantidad de elementos de la lista mayor
    for i in range(0,mayor):
        import random
        #Se realiza un condicional, esto con el fin de que cuando el ciclo vaya en la primera vuelta o vuelta 0 no me compare el número aleatorio encontrado, ya que al ser el primer número encontrado no tendrá con quien comparar
        if i!=0:
            #Se halla la cantidad de elementos de la lista que contiene los números aleatorios y se inicializan variables
            long=len(lista_numeros_aleatorios)
            cont=False
            #Se realiza un ciclo while el cual me permitirá realizar el proceso de generar el número aleatorio las veces necesarias, esto con el fin de que el número aleatorio no se repita
            while cont==False:
                #Se genera el número aleatorio
                numero_aleatorio=random.randint(0,mayor-1)
                #Se realiza un ciclo for el cual me permitirá evaluar si el número aleatorio generado ya se encuentra o si por el contrario está disponible en la lista que contiene los números aleatorios
                for i1 in range(0,long):
                    #Se realiza un condicional, esto con el fin de comparar el número generado con el elemento de la lista que contiene los números aleatorios en la posición i
                    if lista_numeros_aleatorios[i1]==numero_aleatorio:
                        #En caso de que el número ya esté me retornara un por medio de la variable cont un 'False' esto para que por medio del ciclo while se vuelva a realizar el proceso
                        cont=False
                        #Se termina o rompe el ciclo
                        break
                    else:
                        #En caso de que al hacer la comparación el número aleatorio generado sea distinto al número comparado de la lista que contiene los números aleatorios generados, me irá asignando a la variable cont un 'True'
                        cont=True
            #Una vez hallado el número aleatorio me lo agregará a la lista que contiene los números aleatorios generados
            lista_numeros_aleatorios.append(numero_aleatorio) 
        else:
            numero_aleatorio=random.randint(0,mayor)
            lista_numeros_aleatorios.append(numero_aleatorio)
    #Se crea una lista vacía la cual contendrá los elementos de las listas ingresadas de manera aleatoria
    lista_final=[]
    #Se halla la cantidad de números aleatorios generados
    long=len(lista_numeros_aleatorios)
    #Se realiza un ciclo for el cual irá desde 0 hasta la cantidad de números aleatorios generados
    for i in range(0,long):
        #Se realiza un condicional, esto con el fin de separar procedimientos 
        if mayor==menor:
            #En caso de que las dos listas ingresadas tengan la misma cantidad de elementos simplemente se irá agregando a la 'lista_final' sus elementos en la posición i
            lista_final.append(lista_mayor[lista_numeros_aleatorios[i]])
            lista_final.append(lista_menor[lista_numeros_aleatorios[i]])
        else:
            #En caso de que las dos listas ingresadas no tengan la misma cantidad de elementos se tendrá que evaluar si el número de la lista de los números aleatorios generados es mayor o igual a la cantidad de elementos de la lista menor
            if lista_numeros_aleatorios[i]>=menor:
                #Si el número de la lista de números aleatorios generados es mayor o igual a la lista con menor cantidad de elementos, simplemente se ingresará a la 'lista_final' el elemento de la lista mayor en la posición i, esto ya que si se tratará de ingresar también el elemento de la lista menor en la posición i se saldría de rango
                lista_final.append(lista_mayor[lista_numeros_aleatorios[i]])
            else:
                #Si el número de la lista de números aleatorios generados es menor a la lista con menor xantidad de elementos, se ingresará a la 'lista_final' el elemento de la lista mayor y menor en la posición i
                lista_final.append(lista_mayor[lista_numeros_aleatorios[i]])
                lista_final.append(lista_menor[lista_numeros_aleatorios[i]])
    #Se retorna la lista de nombre 'lista_final'
    return lista_final

def Loteria(paquete):
    long=len(paquete)
    for i in range(0,long):
        for i1 in range(i,long):
            if paquete[i]==paquete[i1]:
                comentario="Hay elementos duplicados"
                break
            else:
                comentario="No hay elementos duplicados"
        break

    long_premium=len(premium)
    cont_cartas_premium=0
    for i in range(0,long):
        for i1 in range(i,long_premium):
            if paquete[i]==premium[i1]:
                cont_cartas_premium+=1
                if cont_cartas_premium>1:
                    comentario_1="Hay más de una carta premium"
                    break
            else:
                comentario_1="No hay más de una carta premium"
        break
    
    import random
    if comentario=="Hay elementos duplicados" and comentario_1=="No hay más de una carta premium":
        numero_aleatorio_premium=random.randint(0,long_premium-1)
        carta_premium=premium[numero_aleatorio_premium]
        for i in range(0,long):
            if carta_premium==paquete[i]:
                comentario="No se pudo agregar la carta premium"
                break
            else:
                comentario="Si se pudo agregar la carta premium"
        
    if comentario=="Si se pudo agregar la carta premium":
        for i in range(0,long):
            for i1 in range(0,long_premium):
                if paquete[i]==premium[i1]:
                    posición_carta_premium=paquete[i]
                    comentario=True
                    break
                else:
                    comentario=False
            break
        if comentario==False:
            paquete.remove(paquete[random.randint(0,long-1)])
            paquete.append(carta_premium)
        else:
            cont=False
            while cont==False:
                numero_aleatorio=random.randint(0,long-1)
                if numero_aleatorio==posición_carta_premium:
                    cont=False
                else:
                    cont=True
            paquete.remove(paquete[numero_aleatorio])
            paquete.append(carta_premium)
    return paquete            
    
Imprimir(cartas)
Imprimir(premium)
jugador=Generador(cartas,10)
juego=Combinador(cartas,premium)
sobre_uno=Generador(juego,5)
sobre_dos=Generador(juego,5)
sobre_tres=Generador(juego,5)
sobre_uno_y_dos=Combinador(sobre_uno,sobre_dos)
paquete=Combinador(sobre_uno_y_dos,sobre_tres)
paquete_final=Loteria(paquete)
print(paquete_final)

"@author: user"