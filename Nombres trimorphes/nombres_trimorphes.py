limiteMin=int(input())
limiteMax=int(input())
for n in range(limiteMin,limiteMax+1):
    if n%10 in [0,1,4,5,6,9]:
        if int(str(n**3)[-len(str(n)):])==n:
            print(n)
