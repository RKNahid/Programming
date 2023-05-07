a,b,c,d=map(int,input().split())
dif = ((c*60)+d)-((a*60)+b)
if dif<=0:
    dif+=24*60
t = dif//60
m = dif%60
print("O JOGO DUROU",t,"HORA(S) E",m,"MINUTO(S)")
