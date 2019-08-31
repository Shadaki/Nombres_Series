from math import *
limiteMin=int(input())
limiteMax=int(input())
for nombre in range(limiteMin,limiteMax+1):
    somme=0
    for y in range(2,ceil(sqrt(nombre))):
        if nombre%y==0: somme+=y+nombre/y
    if nombre<somme: print(nombre)
