limiteMin=int(input())
limiteMax=int(input())
n=0
while n*(7*n-5)/2<limiteMin:
    n+=1
while n*(7*n-5)/2<limiteMax:
    print(int(n*(7*n-5)/2))
    n+=1
