limiteMin=int(input())
limiteMax=int(input())
n=0
while n*(3*n-1)/2<limiteMin:
    n+=1
while n*(3*n-1)/2<limiteMax:
    print(int(n*(3*n-1)/2))
    n+=1
