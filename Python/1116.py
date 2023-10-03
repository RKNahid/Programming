n = int(input())
for x in range(n):
    a,b=map(int,input().split())
    if b==0:
        print("divisao impossivel")
    else:
        c=float(a/b)
        print("%.1f"%c)
