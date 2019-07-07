limiteMin=int(input())
limiteMax=int(input())
n=0
while n*(2*n-1)<limiteMin:
    n+=1
while n*(2*n-1)<limiteMax:
    print(n*(2*n-1))
    n+=1
