limiteMin=int(input())
limiteMax=int(input())
for n in range(limiteMin,limiteMax+1):
    if n%sum([int(x) for x in list(str(n))])==0: print(n)
    
