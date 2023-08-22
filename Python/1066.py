x = range(0,5)
e = 0
o = 0
p = 0
n = 0
for i in x:
    i = float(input())
    if i%2==0:
        e=e+1
    if i%2==1:
        o=o+1
    if i>0:
        p=p+1
    if i<0:
        n=n+1

print(e,"valor(es) par(es)")
print(o,"valor(es) impar(es)")
print(p,"valor(es) positivo(s)")
print(n,"valor(es) negativo(s)")

