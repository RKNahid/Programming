a,b,c = map(float, input().split())
p = float(0.5*a*c)
q = float(3.14159*c*c)
r = float(((a+b)/2)*c)
s = b*b
t = a*b
print("TRIANGULO: %.3f"%p)
print("CIRCULO: %.3f"%q)
print("TRAPEZIO: %.3f"%r)
print("QUADRADO: %.3f"%s)
print("RETANGULO: %.3f"%t)
