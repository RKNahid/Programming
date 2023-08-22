a = int(input())
p,q=0,0
for i in range(0,a):
    b = int(input())
    if 10<=b<=20:
        p+=1
    else:
        q+=1
print(p,"in")
print(q,"out")
