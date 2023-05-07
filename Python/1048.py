a = float(input())

if 0.00 <= a <= 400.00:
    r = float(a*(15/100))
    print("Novo salario: %.2f"%(a+r))
    print("Reajuste ganho: %.2f"%r)
    print("Em percentual: 15 %")
elif 400.01 <= a <= 800.00:
    r = float(a*(12/100))
    print("Novo salario: %.2f" % (a+r))
    print("Reajuste ganho: %.2f"%r)
    print("Em percentual: 12 %")
elif 800.01 <= a <= 1200.00:
    r = float(a*(10/100))
    print("Novo salario: %.2f" % (a+r))
    print("Reajuste ganho: %.2f"%r)
    print("Em percentual: 10 %")
elif 1200.01 <= a <= 2000.00:
    r = float(a*(7/100))
    print("Novo salario: %.2f" % (a+r))
    print("Reajuste ganho: %.2f"%r)
    print("Em percentual: 7 %")
else:
    r = float(a*(4/100))
    print("Novo salario: %.2f" % (a+r))
    print("Reajuste ganho: %.2f"%r)
    print("Em percentual: 4 %")
