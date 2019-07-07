limiteMin=int(input())
limiteMax=int(input())
n=0
while (n**3+5*n+6)/6<limiteMin:
    n+=1
while (n**3+5*n+6)/6<limiteMax:
    print(int((n**3+5*n+6)/6))
    n+=1
