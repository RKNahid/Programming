a = int(input())
for i in range(0,a):
    b = int(input())
    if b == 0:
        print("NULL")
    elif b%2!=0 and b<0:
        print("ODD NEGATIVE")
    elif b%2!=0 and b>0:
        print("ODD POSITIVE")
    else:
        if b>0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
