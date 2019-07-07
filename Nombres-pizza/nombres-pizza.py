limiteMin=int(input())
limiteMax=int(input())
n=0
while (n**2+n+2)/2<limiteMin:
    n+=1
while (n**2+n+2)/2<limiteMax:
    print(int((n**2+n+2)/2))
    n+=1
