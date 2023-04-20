import math
a,b = map(float, input().split())
c,d = map(float, input().split())
r = math.sqrt(((c-a)*(c-a))+((d-b)*(d-b)))
print("%.4f"% r)
