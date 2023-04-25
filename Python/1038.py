a,b = map(float,input().split())
p = 0
if a==1:
    p = 4.00*b
elif a==2:
    p = 4.50*b
elif a==3:
    p = 5.00*b
elif a==4:
    p = 2.00*b
elif a==5:
    p = 1.50*b
print("Total: R$ %.2f"%p)
