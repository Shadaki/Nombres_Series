limiteMin=int(input())
limiteMax=int(input())
for nombre in range(limiteMin,limiteMax+1):
    somme=0
    for y in range(1,nombre):
        if nombre%y==0: somme+=y
    if nombre<somme: print(nombre)