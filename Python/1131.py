#runtime error

i,g,e,m=0,0,0,0
while 1:
    a,b=list(map(int,input().split()))
    m+=1
    if a>b:
        i+=1
    elif a<b:
        g+=1
    else:
        e+=1
    t=0
    while 1:
        print("novo granal (1-sim 2-nao)")
        t = int(input())
        if t==1:
            continue
        if t==2:
            break
print(m,"grenais")
print("Inter:{}".format(i))
print("Gremio:{}".format(g))
print("Empates:{}".format(e))
if i>g:
    print("Inter venceu mais")
elif g>i:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
