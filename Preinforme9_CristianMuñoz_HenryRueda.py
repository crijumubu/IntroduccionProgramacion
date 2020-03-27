# -*- coding: utf-8 -*-

#created on Thu Mar 26 19:53:58 2020
#%% Ejercicio 19

X1=int(input("Ingrese el valor de X1: "))
Y1=int(input("Ingrese el valor de Y1: "))
X2=int(input("Ingrese el valor de X2: "))
Y2=int(input("Ingrese el valor de Y2: "))
print("La distancia entre los puntos es: " + str(((X2-X1)**2+(Y2-Y1)**2)**1/2))

#%% Ejercicio 23

n=int(input("Ingrese un número de 4 dígitos:"))
a=n%10
b=((n-a)/10)%10
c=((((n-a)/10)-b)/10)%10
d=(((((n-a)/10)-b)/10)-c)/10
z=int(a*1000+b*100+c*10+d)
print(z)

#%% Ejercicio 30

n1=float(input("Ingrese el valor de n1: "))
n2=float(input("Ingrese el valor de n2: "))
n3=float(input("Ingrese el valor de n3: "))
n4=float(input("Ingrese el valor de n4: "))
n5=float(input("Ingrese el valor de n5: "))

a=n1*0.15
b=n2*0.20
c=n3*0.15
d=n4*0.30
e=n5*0.20
nf=a+b+c+d+e
print(nf)

if nf<=2.0:
    print("No puede habilitar")
elif nf<3.0:
    print("Usted ha reprobado")
elif nf<=4.5:
    print("Usted aprobó")
elif nf>4.5:
    print("Felicitaciones")

#%% Ejercicio 60

c=1
a=1
cont=0
n=int(input("Ingrese la cantidad de filas: ")

while cont!=0
    print(c)
    a=(10*(10**cont))+a
    c=a+c
    cont=cont+1
    
"@author: user"