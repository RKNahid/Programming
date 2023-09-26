n = int(input())
c,r,s,f=0,0,0,0
for i in range(n):
    a,ch=list(map(str,input().split()))
    a = int(a)
    if ch=='C':
        c+=a
    elif ch=='R':
        r+=a
    else:
        s+=a
f=c+r+s
x = (c * 100.00) / f
y = (r * 100.00) / f
z = (s * 100.00) / f
print("Total: {} cobaias".format(f))
print("Total de coelhos:", c)
print("Total de ratos:", r)
print("Total de sapos:", s)
print("Percentual de coelhos: %.2f %%"%x)
print("Percentual de ratos: %.2f %%"%y)
print("Percentual de sapos: %.2f %%"%z)
