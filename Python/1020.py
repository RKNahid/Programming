
a = int(input())
h = 0
m = 0
if a>364:
    h = int(a/365)
    a = a%365
    m = int(a/30)
    a = a%30
    print(h,"ano(s)")
    print(m,"mes(es)")
    print(a,"dia(s)")
elif a<365 and a>29:
    m = int(a/30)
    a = a%30
    print(h, "ano(s)")
    print(m, "mes(es)")
    print(a, "dia(s)")
else:
    print(h, "ano(s)")
    print(m, "mes(es)")
    print(a, "dia(s)")
