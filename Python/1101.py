while 1:
    s,r=0,''
    a,b=map(int,input().split())
    if a<=0 or b<=0:
        break
    else:
        if a > b:
            a, b = b, a
        for p in range(a, b + 1):
            r += str(p) + ' '
            s += p
        r += 'Sum=%d'
        print(r % s)
