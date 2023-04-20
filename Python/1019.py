a = int(input())
if a>3600:
    h = int(a/3600)
    a = a%3600
    m = int(a/60)
    a = a%60
    print("%d:%d:%d"%(h,m,a))
elif a<3600 and a>60:
    m = int(a/60)
    a = a%60
    print("0:%d:%d"%(m,a))
else:
    print("0:0:%d"% a)
