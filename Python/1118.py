while 1:
    c,d=0,0
    while 1:
        if(d==2):
            break
        a=float(input())
        if 0<=a<=10:
            d+=1
            c+=a
        else:
            print("nota invalida")
    b=c/2.00
    print("media = %.2f"%b)
    t=0
    while 1:
        print("novo calculo (1-sim 2-nao)")
        t=int(input())
        if t==1 or t==2:
            break

