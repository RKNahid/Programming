a = int(input())
b = int(input())
s=0
c = range((b+1),a)
for i in c:
    if i%2!=0:
        s+=i
print(s)
