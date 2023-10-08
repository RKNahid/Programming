a,g,d=0,0,0
while 1:
    n=int(input())
    if n==1:
        a+=1
    elif n==2:
        g+=1
    elif n==3:
        d+=1
    elif n==4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool:",a)
print("Gasolina:",g)
print("Diesel:",d)



