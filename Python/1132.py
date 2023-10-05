a=int(input())
b=int(input())
s=0
if a>b:
    a,b=b,a
for i in range(a,b+1):
    if i%13!=0:
        s+=i
print(s)
