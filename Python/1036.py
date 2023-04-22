import math

a,b,c = map(float, input().split())
r = ((b*b)-4*a*c)
if r<0 or a==0:
    print("Impossivel calcular")
else:
    t = math.sqrt(r)
    r1 = (-b+t)/(2*a)
    r2 = (-b-t)/(2*a)
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)
