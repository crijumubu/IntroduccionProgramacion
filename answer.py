# -*- coding: utf-8 -*-

p=int(input("Ingrese el peso del paquete en kilogramos: "))
d=int(input("Ingrese la distancia del viaje en kilómetros: "))
v=int(input("Ingrese 1 si el vuelo es nacional o 2 si el vuelo es intercontinental: "))

if p>10:
    if p<237500:
        if v==1:
            p1=4500*p
            d1=4000*d
            if p>100:
                t=(p1+d1)*(85/100)
                print("El precio del envío es de:", t, "pesos")
            else:
                t=p1+d1
                print("El precio del envío es de:", t, "pesos")
        else:
            p2=4500*p
            d2=8000(d*0.621371)
            if d>8000 and p>400:
                t=(p2+d2)*(90/100)
                print("El precio del envío es de:", t, "pesos")
            else:
                t=p2+d2
                print("El precio del envío es:", t, "pesos")
    elif p<=250000: 
         print("Dejar de pedir paquetes y finalizar el proceso de carga")
    else:
        print("El peso supera el límite de carga de la aeronave")
else:
    print("El peso no es aceptable")
    