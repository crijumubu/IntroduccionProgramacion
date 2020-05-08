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

#PARTE A

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

#Punto 9

def Loteria(paquete,jugador):
    #Se calcula la cantidad de elementos del paquete
    long=len(paquete)
    #Se realiza un ciclo for desde 0 hasta la cantidad de elementos
    for i in range(0,long):
        #Se realiza un ciclo for desde 'i' hasta la cantidad de elementos, se inicia en 'i' ya que no se necesita volver a comparar los elementos ya comparados anteriormente, se prodia inicar en 0 pero sería un poco menos eficiente
        for i1 in range(i,long):
            #Se realiza un condicional el cual me permitirá saber si hay elementos repetidos, si encuentra un elemento repetido me retornará un mensaje por medio de la variable 'comentario' y el ciclo se acabará
            if paquete[i]==paquete[i1]:
                comentario="Hay elementos duplicados"
                break
            else:
                comentario="No hay elementos duplicados"
        #Se realiza un condicional el cual me permitirá saber si hubieron elementos repetidos, si hubieron elementos repetidos el ciclo llegará a su fin, sino el ciclo seguirá evaluando la lista 'paquete' en busca de elementos repetidos     
        if comentario=="Hay elementos duplicados":
            break
    
    #Se halla la cantidad de elementos de la lista de cartas premium y se inicializan variables
    long_premium=len(premium)
    cont_cartas_premium=0
    #Se realiza un ciclo for desde 0 hasta la cantidad de elementos del paquete
    for i in range(0,long):
        #Se realiza un ciclo for desde i hasta la cantidad de elementos de la lista de cartas premium, se inicia en 'i' ya que no se necesita volver a comparar los elementos ya comparados anteriormente, se prodia inicar en 0 pero sería un poco menos eficiente
        for i1 in range(i,long_premium):
            #Se realiza un condicional el cual me permitirá saber si hay cartas premium en el paquete, si hay cartas premium en el paquete me le sumará de a uno al contador de nombre 'cont_cartas_premium'
            if paquete[i]==premium[i1]:
                cont_cartas_premium+=1
                #Se realiza un condicional el cual me permitirá saber si hay mas de una carta premium en el paquete, si así lo es, me dará un mensaje por medio de la variable 'comentario_1' y el ciclo llegará a su fin
                if cont_cartas_premium>1:
                    comentario_1="Hay más de una carta premium"
                    break
            else:
                comentario_1="No hay más de una carta premium"
        #Se realiza un condicional el cual me permitirá saber si hubieron más de una carta premium en el paquete, si hubieron más de una carta premium en el paquete el ciclo llegará a su fin, sino el ciclo seguirá evaluando la lista 'paquete' para ver si tiene más de una carta premium
        if comentario_1=="Hay más de una carta premium":
            break
    
    import random
    #Se realiza un condicional el cual me permitirá ver si se cumplieron o no las dos condiciones planteados en el enunciado del ejercicio
    if comentario=="Hay elementos duplicados" and comentario_1=="No hay más de una carta premium":
        #Se crea un número aleatorio en el rango de 0 hasta la cantidad de cartas premium menos 1, menos 1 ya ue este rango me incluye el valor final del rango, si me lo incluyera se saldría del rango al evaluar este valor en la lista de cartas premium
        numero_aleatorio_premium=random.randint(0,long_premium-1)
        #Se guarda en una variable la carta premium en esta posición
        carta_premium=premium[numero_aleatorio_premium]
        #Se realiza un ciclo desde 0 hasta la cantidad de elementos del paquete
        for i in range(0,long):
            #Se evalua la carta premium en el paquete para evaluar si ya se encuentrá, si así lo es me retornará un comentario y si aún no se encuentra me retornará otro comentario
            if (carta_premium in paquete[i]) or (carta_premium in jugador):
                comentario="No se pudo agregar la carta premium"
                break
            else:
                comentario="Si se pudo agregar la carta premium"
    
    #Se realiza un condicional para mirar que comentario me retorno en el paso anterior
    #Si el comentario es 'Si se pudo agregar la carta premium' se hara el siguiente procedimiento, sino no se hará nada
    if comentario=="Si se pudo agregar la carta premium":
        #Se realiza un ciclo for que inicia en 0 hasta la cantidad de elementos del paquete
        for i in range(0,long):
            #Se realiza un ciclo for que inicia en 0 hasta la cantidad de elementos de la lista de cartas premium
            for i1 in range(0,long_premium):
                #Se realiza un condicional el cual me permitirá saber la posición de la carta premium que tiene el paquete en caso de que tenga, esto con el fin de que cuando se vaya a anexar la carta premium aleatoria en el paquete no se vaya a anexar en esta posición
                if paquete[i]==premium[i1]:
                    posición_carta_premium=paquete[i]
                    comentario=True
                    break
                else:
                    comentario=False
            #Se realiza un condicional el cual me permitirá saber si encontró la posición de la carta en el paquete, si así lo es el ciclo llegará a su fin, sino el ciclo continuará
            if comentario==True:
                    break
        #Se realiza un condicional, en caso de que el paquete no tuviera ninguna carta premium se anexará la carta premium aleatoria y se eliminará una de las cartas que ya tenía
        if comentario==False:
            paquete.remove(paquete[random.randint(0,long-1)])
            paquete.append(carta_premium)
        #En caso de que el paquete si tuviera una carta premium se hará lo siguiente:
        else:
            #Se inicializa variables
            cont=False
            #Se realiza un ciclo while el cual parará cuando la variable 'cont' sea distinto a 'False'
            while cont==False:
                #Se genera un número aleatorio en el rango de 0 hasta la cantidad de elementos del paquete menos 1, la razón del menos 1 se explicó anteriormente
                numero_aleatorio=random.randint(0,long-1)
                #Se realiza un condicional el cual me permitirá saber si el número generado es igual a la posición de la carta premium en el paquete, si así lo es se generará otra vez el número aleatorio, sino el ciclo llegará a su fin
                if numero_aleatorio==posición_carta_premium:
                    cont=False
                else:
                    cont=True
            #Se elimina la carta del paquete en la posición del número aleatorio generado anteriormente
            paquete.remove(paquete[numero_aleatorio])
            #Se agrega la carta premium aleatoria al paquete
            paquete.append(carta_premium)
    #Se retorna la lista de nombre paquete
    return paquete 

#Punto 10

def jugador_y_paquete(paquete_final,jugador):
    #Se halla la cantidad de elementos del paquete
    long_paquete=len(paquete_final)
    #Se realiza un ciclo desde 0 hasta la cantidad de elementos del paquete, por medio de este ciclo se agregarán las cartas del paquete a las cartas del jugador
    for i in range(0,long_paquete):
        jugador.append(paquete_final[i])
    #Se retorna la lista de nombre 'jugador'
    return jugador

def Punto10(jugador,premium):
    #Punto 10.1
    #Se halla la cantidad de elemntos de la lista 'jugador' y 'premium' y se inicializa una lista vacía la cual contendrá las cartas premium que tiene la lista jugador
    long_jugador=len(jugador)
    long_premium=len(premium)
    cartas_premium_en_jugador=[]
    #Se realiza un ciclo for desde 0 hasta la cantidad de elementos de la lista jugador
    for i in range(0,long_jugador):
        #Se realiza un ciclo for desde 0 hasta la cantidad de elementos de la lista premium
        for i1 in range(0,long_premium):
            #Se realiza un condicional para verificar si la carta de la lista 'jugador' en la posición i es igual a la lista de cartas 'premium' en la posición i1
            if jugador[i]==premium[i1]:
                #En caso de que dicha condición se cumpla se agregará la carta premium a la lista que se había inicializado
                cartas_premium_en_jugador.append(jugador[i])
    #Se halla la cantidad de elementos de la lista de nombre 'long_cartas_premium_en_jugador', esta lista es la que contiene las cartas premium de la lista 'jugador'
    long_cartas_premium_en_jugador=len(cartas_premium_en_jugador)
    #Se realiza un condicional el cual me permitirá saber si la cantidad de lementos de dicha lista es igual a 0 o no
    if long_cartas_premium_en_jugador==0:
        #En caso de que dicha condición se cumpla me imprimirá que no hay cartas premium
        print("El jugador no tuvo cartas premium")
    else:
        #En caso de que dicha condición no se cumpla me imprimirá las cartas premium que tiene el jugador
        print("Las cartas premium fueron las siguientes: ",cartas_premium_en_jugador )
    
    #Punto 10.2
    
    #Se inicializa variables
    cont_cartas_repetidas=0
    #Se realiza un ciclo que va desde 0 hasta la cantidad de elementos de la lista 'jugador'
    for i in range(0,long_jugador):
        #Se realiza un ciclo for que vas desde 'i+1' hasta la cantidad de elementos de la lista 'jugador', 'i+1' ya que no necesitamos volver a comparar los elementos que ya hemos comparados, se podría iniciar el ciclo for en 0 pero sería un poco más ineficiente
        for i1 in range(i+1,long_jugador):
            #Se realiza un condicional el cual me permitirá saber si hay cartas iguales y me irá sumando de a uno al contador cada vez que está condición se cumpla
            if jugador[i]==jugador[i1]:
                cont_cartas_repetidas+=1
    #Se imprime la cantidad de cartas repetidas que tuvo el jugador
    print("El jugador tuvo",cont_cartas_repetidas,"carta/s repetida/s")
    
    #Punto 10.3
    
    print("La cantidad de veces que aparece cada carta en la lista final de cartas del jugador es:")
    #Se crea una copia de la lista jugador y se inicializan variables
    jugador_copia=jugador.copy()
    cont_cartas=1
    #Se realiza un ciclo for que va desde 0 hasta la cantidad de elementos de la lista 'jugador'
    for i in range(0,long_jugador):
        #Se halla la cantidad de elementos de la lista copia
        long_jugador_copia=len(jugador_copia)
        #Se realiza un ciclo for el cual irá desde 'i+1' hasta la cantidad de elemntos de la lista copia menos, 'i+1' debido a la razón ya antes explicado y la cantidad de elementos de la lista copia menos 1 debido a que cada vez se eliminará por lo menos un elemento de la lista
        for i1 in range(i+1,long_jugador_copia-1):
            #Se realiza un condicional el cual me permitirá saber si la carta se repite y si es así me irá sumando de a uno al contador y me eliminará la coincidencia de dicha carta
            if jugador[i]==jugador_copia[i1]:
                cont_cartas+=1
                jugador_copia.remove(jugador_copia[i1])
        #Se imprime la carta con su respectiva cantidad de veces que se repite
        print(jugador[i],':',cont_cartas)
        #Se deja el contador en su valor inicial
        cont_cartas=1
        
    #Punto 10.4
    
    #Se crea una lista con las letras del alfabeto ingles y se inicializa una lista vacia
    alfabeto=['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letras=[]
    #Se crea un ciclo for que vaya de carta en carta en la lista 'jugador'
    for carta in jugador:
        #Se crea un ciclo for que vaya de letra en letra en cada carta
        for letra in carta:
            #Se pasa la letra a minúscula
            letra=letra.lower()
            #Se agrega dicha letra a la lista que habiamos inicializado anteriormente
            letras.append(letra)
            #Se rompe el ciclo ya que solo necesitamos la primera letra de cada comentario
            break
    
    #Se halla la cantidad de elemento de la lista que contiene las letras del alfabeto inglés
    long_alfabeto=len(alfabeto)
    #Se realiza un ciclo for el cual vaya desde 0 hasta la cantidad de elementos de la lista que contiene las letras del alfabeto inglés
    for i in range(0,long_alfabeto):
        #Se inicializan variables
        cont=0
        #Se realiza un ciclo for el cual va desde 0 hasta la cantidad de elementos de la lista 'jugador'
        for i1 in range(0,long_jugador):
            #Se realiza un condicional el cual me permitirá comparar las letras del alfabeto con las letras iniciales de las cartas
            if alfabeto[i]==letras[i1]:
                #Cada vez que encuentre coincidencias me irá sumando de a uno al contador
                cont+=1
        #Se imprime la letra con su respectiva cantidad de veces que es la letra inicial de las cartas 
        print(alfabeto[i],':',cont)
        
    #Punto 10.5
    
    #Se inicializan variables
    mayor=len(jugador[0])
    menor=len(jugador[0])
    #Se realiza un ciclo for que inicie en 0 y termine en la longitud de elementos de la lista 'jugador'
    for i in range(0,long_jugador):
        #Se realiza un condicional que me permitirá conocer el mayor
        if mayor<len(jugador[i]):
            mayor=len(jugador[i])
            carta_mayor=jugador[i]
        #Se realiza un elif el cual en caso de que la primera condición no se cumpla, me evaluará la segunda condición, este elif me permitirá encontrar el menor
        elif menor>len(jugador[i]):
            menor=len(jugador[i])
            carta_menor=jugador[i]
    #Se imprime la carta más larga o mayor y la carta más corta o menor
    print("La carta que tiene el nombre con la longitud más larga es:",carta_mayor)
    print("La carta que tiene el nombre con la longitud más corta es:",carta_menor)
    
    #Punto 10.6
    
    #Se realiza un condicional para determinar si hay cartas premium en la lista jugador, esto con base en listas anteriormente creadas, esto con el fin de no volver a hacer todo el procedimiento
    if long_cartas_premium_en_jugador!=0:
        #Se crea una lista vacía la cual contendrá las iniciales le cartas premium
        iniciales_cartas_premium=[]
        #Se realiza un ciclo for desde 0 hasta la cantidad de elementos de las cartas premium
        for i in range(0,long_cartas_premium_en_jugador):
            #Se realiza un ciclo for que va de carta en carta en la lista de cartas premium del jugador
            for cartas_premium in cartas_premium_en_jugador:
                #Se realiza un ciclo for que va de letra en letra en cada carta premium
                for letra in cartas_premium:
                    #Se transforma la letra a minúscula
                    letra=letra.lower()
                    #Se agrega esta letra a la lista que habíamos inicializado antes
                    iniciales_cartas_premium.append(letra)
                    #Se rompe el ciclo ya que solo queremos que nos tome la primera letra, es decir que nos haga una iteración
                    break
        
        #Se crea una lista vacía la cual contendrá las letras finales de las cartas
        letras_finales_cartas=[]
        #Se realiza un ciclo for que va desde 0 hasta la cantidad de elementos de la lista jugador
        for i in range(0,long_jugador):
            #Se accede a la última letra de la carta y se convierte a minúscula y se agrega a la lista
            letra_final=jugador[i][-1].lower()
            letras_finales_cartas.append(letra_final)
        
        #Se inicializan variables y se halla la cantidad de elementos de la lista que tiene las iniciales de la/s carta/s premium
        cont=0
        long=len(iniciales_cartas_premium)
        #Se realiza un ciclo for el cual va desde 0 hasta la cantidad de elementos de la lista jugador
        for i in range(0,long_jugador):
            #Se realiza un ciclo for el cual va desde 0 hasta la cantidad de elementos de la lista que tiene las iniciales de la/s carta/s premium
            for i1 in range(0,long):
                #Se realiza un condicional el cual me permitirá saber si la letra final de la carta en la posición i es igual a la letra inicial de la carta premium en la posición i1
                if letras_finales_cartas[i]==iniciales_cartas_premium[i1]:
                    #Si la condición se cumple me irá sumando de a uno al contador
                    cont+=1
        #Se imprime el resultado
        print("La cantidad de cartas que terminan con la letra con la que empieza la(s) cartas premium obtenidas en las cartas finales del jugador es",cont)
    else:
        #Si la condición no se cumple se imprimirá que no tiene cartas premium
        print("No tiene cartas premium")
        
    #Punto 10.7
    
    #Se imprime lo que se va a realizar
    print("Letras que aparecen escritas dos o más veces de forma consecutiva en el nombre de las cartas finales del jugador:")
    #Se realiza un ciclo for que va desde 0 hasta la cantidad de elementos de la lista del jugador
    for i in range(0,long_jugador):
        #Se halla la cantidad de elementos de la carta es decir de la lista jugador en la posición i y se inicializan variables
        long=len(jugador[i])
        cont=0
        letra=[]
        #Se realiza un ciclo for que va desde 0 hasta la cantidad de elementos de la carta menos 1, menos 1 porque siempre compararemos con el que le sigue es decir por ejemplo, jugador[0][0], lo compararemos con jugador[0][1] y así sucesivamente
        for i1 in range(0,long-1):
            #Se realiza un condicional para saber si la letra es igual a la letra que le sigue
            if jugador[i][i1]==jugador[i][i1+1]:
                #Si la condición se cumpla se sumará uno al contador
                cont+=1
                letra.append(jugador[i][i1])
        #Se realiza un condicional para mirar si hubieron letras escritas de forma consecutiva con base en el contador
        if cont>=1:
            #Se imprime la carta y la cantidad de veces que aparecen las repeticiones
            print("En la carta",jugador[i],"hay letras escritas de forma consecutiva y estas repeticiones aparecen",cont,"vez/veces, la/s letra/s que se repite/n es/son:",letra)
        else:
            #Se imprime la carta y se dice que no hay letras escritas de forma consecutiva
            print("En la carta",jugador[i],"NO hay letras escritas de forma consecutiva")
    
    #Punto 10.8
    
    #Se imprime lo que se va a realizar
    print("Las veces que está representada las letras del alfabeto inglés en los de todas las cartas de la lista final de cartas del jugador es: ")
    #Se realiza un ciclo for que va desde 0 hasta la cantidad de elementos del alfabeto inglés
    for i in range(0,long_alfabeto):
        #Se inicializan variables
        cont=0
        #Se realiza un ciclo for que irá de carta en carta en la lista jugador
        for cartas in jugador:
            #Se realiza un ciclo for que irá de letra en letra en cada carta
            for letras in cartas:
                #Se transforma la letra a minúscula
                letras=letras.lower()
                #Se realiza un condicional para mirar si el alfabeto en la posición i es igual a la letra
                if alfabeto[i]==letras:
                    #Si se cumple la condición se sumará de a uno al contador
                    cont+=1
        #Se imprime el resultado
        print(alfabeto[i],':',cont)
        
Imprimir(cartas)
Imprimir(premium)
jugador=Generador(cartas,10)
juego=Combinador(cartas,premium)
#Punto 7
sobre_uno=Generador(juego,5)
sobre_dos=Generador(juego,5)
sobre_tres=Generador(juego,5)
#Punto 8
sobre_uno_y_dos=Combinador(sobre_uno,sobre_dos)
paquete=Combinador(sobre_uno_y_dos,sobre_tres)
paquete_final=Loteria(paquete,jugador)
jugador_final=jugador_y_paquete(paquete_final,jugador)
print("La lista del jugador quedó de la siguiente manera:")
Imprimir(jugador_final)
Punto10(jugador_final,premium)

#%%PARTE B

respuesta='YES'
partidas_ganados_jugador=0
partidas_ganados_tallador=0
partidas_en_total=0
while respuesta=='YES':
    #Punto 11
        
    Ponderado={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
           '8':8,'9':9,'J':10,'Q':10,'K':10}

    #Punto 12
    
    Simbolos=['C','D','T','P']

    #Punto 13

    def Combinar(Ponderado,Simbolos):
        #Se inicializa el diccionario vacío de nombre 'Baraja'
        Baraja={}
        #Se realiza un ciclo for que va de clave en clave en el diccionario de nombre 'Ponderado'
        for key in Ponderado:
            #Se realiza un ciclo for que va de elemento en elemento en la lista de nombre 'Simbolos'
            for elemento in Simbolos:
                #Se agrega al diccionario vacío la clave junto con el símbolo y se le asigna el valor de la clave 
                Baraja[key+elemento]=Ponderado[key]
                #Se retorna el diccionario de nombre 'Baratija'
        return Baraja

    #Punto 14

    def Revolver(Baraja):
        #Se halla la cantidad de llaves del diccionario y se crea una lista vacía la cual contendrá los valores de la llaves
        long=len(Baraja) 
        valores=[]
        #Se realiza un ciclo for el cual vaya de llave en llave en el diccionario, me tome el valor y me lo lleve a la lista 'valores'
        for key in Baraja:
            valores.append(Baraja[key])
    
        import random
        #Se realiza un una copia de la lista valores
        valores_desordenados=valores.copy()
        #Gracias a la librería random podemos desordenar la lista de valores
        random.shuffle(valores_desordenados,random.random)
    
        #Creamos un diccionario vacío que tendrá mi baraja ya revuelta
        Baraja_final={}
        #Se realiza un ciclo for que va desde 0 hasta la cantidad de llaves de la baraja
        for i in range(0,long):
            #Se realiza un ciclo for que va de llave en llave en el diccionario
            for key in Baraja:
                #Se realiza un condicional el cual me permitirá saber a que llave le pertenece el valor
                if valores_desordenados[i]==Baraja[key]:
                    #Se agrega la llave al diccionario vacío y se le asigna el valor 
                    Baraja_final[key]=valores_desordenados[i]
                    #Se elimina la llave del diccionario inicial (Baraja) esto con el fin de que no se vuelva a repetir
                    del Baraja[key]
                    #Se rompe el ciclo
                    break
        #Se retorna el diccionario de nombre 'Baraja_final'
        return Baraja_final
    
    #Punto 16    

    def Repartir(Baraja_final,cartas):
        #Se halla la cantidad de elementos de la lista de las cartas 
        long_cartas=len(cartas)
        #Se crea una lista vacía que tendrá los valores de las llaves de la baraja
        valores=[]
        #Se realiza un ciclo for el cual vaya de llave en llave en el diccionario, me tome el valor y me lo lleve a la lista 'valores'
        for key in Baraja_final:
            valores.append(Baraja_final[key])
    
        import random
        #Se halla la cantidad de elementos de la lista 'valores'
        long=len(valores)
        #Se crea un diccionario copia 
        Baraja_final_copia=Baraja_final.copy()
        #Se realiza un condicional me permite saber cuantas cartas debo darle al usuario según el enunciado
        if long_cartas==0 or long_cartas==1:
            #Se realiza un ciclo for que va desde 0 hasta 2, dos ya que son la cantidad de cartas que debo darle 
            for i in range(0,2):
                #Se genera el número aleatorio en el rango de 0 hasta la cantidad de elementos de la lista valores menos 1
                numero_aleatorio=random.randint(0,long-1)
                #Se realiza un ciclo for el cual va de llave en llave en la baraja
                for key in Baraja_final_copia:
                    #Se realiza un condicional para mirar a a que llave le pertence el valor en la posición del número aleatorio
                    if valores[numero_aleatorio]==Baraja_final_copia[key]:
                        #Se agrega la llave a la lista del jugador, se elimina de la baraja y se acaba el ciclo
                        cartas.append(key)
                        del Baraja_final_copia[key]
                        break
        else:
            #Se genera el número aleatorio en el rango de 0 hasta la cantidad de elementos de la lista valores menos 1
            numero_aleatorio=random.randint(0,long-1)
            #Se realiza un ciclo for que va de llave en llave en la baraja
            for key in Baraja_final_copia:
                #Se realiza un condicional para mirar a a que llave le pertence el valor en la posición del número aleatorio
                if valores[numero_aleatorio]==Baraja_final_copia[key]:
                    #Se agrega la llave a la lista del jugador, se elimina de la baraja y se acaba el ciclo
                    cartas.append(key)
                    del Baraja_final_copia[key]
                    break
        return cartas,Baraja_final_copia
    
    #Punto 17

    def sumar_cartas(Baraja_final,cartas): 
        long=len(cartas)
        suma=0
        for i in range(0,long):
            for key in Baraja_final:
                if cartas[i]==key:
                    suma+=Baraja_final[key]
        return suma
     
    Baraja=Combinar(Ponderado,Simbolos)
    Baraja_final=Revolver(Baraja)
    #Punto 15
    cartas_jugador=[]
    cartas_tallador=[]
    cartas_jugador_final,Baraja_final_copia=Repartir(Baraja_final,cartas_jugador)

    #Punto 18 y 19
    
    #Se le dá información al jugador de la suma de sus cartas
    print("El valor de sus cartas como jugador es",sumar_cartas(Baraja_final,cartas_jugador))
    #Se realiza un condicional en caso de que la suma de las cartas de dé diferente a 21
    if sumar_cartas(Baraja_final,cartas_jugador)!=21:
        #Se le pregunta al usuario si desea otra carta
        respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
        #Se realiza un ciclo for para que cada vez que el usuario digite que 'si' me realice el procedimiento
        while respuesta=='si':
            #Por medio de la función repartir se le da una carta al jugador
            cartas_jugador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_jugador_final)
            #Se calcula la suma de sus cartas y se le muestra al usuario
            suma_jugador=sumar_cartas(Baraja_final,cartas_jugador_final)
            print("El valor de sus cartas como jugador es",suma_jugador)
            #Si la suma es igual a 21 se le informará al usuario y el ciclo se acabará
            if suma_jugador==21:
                print("Usted ya ha completado 21")
                break
            #En caso de que la suma sea mayor a 21 se le informará al usuario que ha perdido debido a que se pasó de 21 y el ciclo llegará a su fin
            elif suma_jugador>21:
                print("Usted ha perdido al pasar de 21")
                break
            #En caso de que ninguna de estas condiciones se cumpla se preguntará al jugador si desea otra carta
            respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
    else:
        #En caso de que la primera condición no se cumpla el usuario habrá ganado automáticamente
        print("Usted ha ganado, felicitaciones!")
    
    #Con las cartas del tallador se hace exactamente el mismo procedimiento que con las cartas del jugador
    cartas_tallador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_tallador)
    print("El valor de sus cartas como tallador es",sumar_cartas(Baraja_final,cartas_tallador))
    if sumar_cartas(Baraja_final,cartas_tallador)!=21:
        respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
        while respuesta=='si':
            cartas_tallador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_tallador_final)
            suma_tallador=sumar_cartas(Baraja_final,cartas_tallador_final)
            print("El valor de sus cartas como tallador es",suma_tallador)
            if suma_tallador==21:
                print("Usted ya ha completado 21")
                break
            elif suma_tallador>21:
                print("Usted ha perdido al pasar de 21")
                break
            respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
    else:
        print("Usted ha ganado, felicitaciones!")
    
    #Se realizan condicionales los cuales me ayudarán a determinar quien fue el ganador de la partida y dependienedo de quien haya ganado me sumará de a uno al contador
    if sumar_cartas(Baraja_final,cartas_jugador_final)>sumar_cartas(Baraja_final,cartas_tallador_final) and sumar_cartas(Baraja_final,cartas_jugador_final)<=21 or sumar_cartas(Baraja_final,cartas_tallador_final)>21:
        print("El jugador ha ganado en esta partida")
        partidas_ganados_jugador+=1
    elif sumar_cartas(Baraja_final,cartas_tallador_final)>sumar_cartas(Baraja_final,cartas_jugador_final) and sumar_cartas(Baraja_final,cartas_tallador_final)<=21 or sumar_cartas(Baraja_final,cartas_jugador_final)>21 or sumar_cartas(Baraja_final,cartas_tallador_final)==sumar_cartas(Baraja_final,cartas_jugador_final):
        print("El tallador ha ganado en esta partida")
        partidas_ganados_tallador+=1
    #Se suma uno al contador de las partidas y se le pregunta al usuario si desea jugar otra partida
    partidas_en_total+=1
    respuesta=input("¿Desea jugar otra partida nueva? Si así lo desea digite 'YES', de lo contrario digite 'NO':")   

#Se imprime el resultado final
print("Se jugaron",partidas_en_total,"partidas en total de las que en",partidas_ganados_jugador,"ganó el jugador y en",partidas_ganados_tallador,"ganó el tallador")

"@author: user"
