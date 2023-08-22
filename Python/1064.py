x = range(0,6)
p = 0
s = 0
for i in x:
    i = float(input())
    if i>0:
        p=p+1
        s = s+i
print(p,"valores positivos")
print("%.1f"%(s/p))
