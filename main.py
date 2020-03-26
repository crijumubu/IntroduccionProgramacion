# -*- coding: utf-8 -*-

a=int(input("Ingrese el valor de a para la ecuación cuadrática: "))
b=int(input("Ingrese el valor de b para la ecuación cuadrática: "))
c=int(input("Ingrese el valor de c para la ecuación cuadrática: "))
d=(b**2)-4*a*c
if d>0:
    x1=(-b+(d**0.5))/(2*a)
    x2=(-b-(d**0.5))/(2*a)
    print("x1=",x1)
    print("x2=",x2)
    if d==0:
        d=-b/(2*a)
        print("d corresponde a:-b/2a que es igual a:", d)
else: 
        print("No existe solución a la ecuación cuadrática dentro del dominio de los números reales")


