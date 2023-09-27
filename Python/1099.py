n = int(input())
for i in range(n):
    s=0
    a,b=map(int,input().split())
    if a>b:
        t=a
        a=b
        b=t
    for p in range(a+1,b):
        if p%2!=0:
            s+=p
    print(s)
