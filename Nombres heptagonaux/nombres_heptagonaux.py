limiteMin=int(input())
limiteMax=int(input())
n=0
while n*(5*n-3)/2<limiteMin:
    n+=1
while n*(5*n-3)/2<limiteMax:
    print(int(n*(5*n-3)/2))
    n+=1
