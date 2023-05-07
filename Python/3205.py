n = int(input())
while n>0:
    n = n-1
    a,b,c = map(int,input().split())
    if c == (b-a):
        print("does not matter")
    elif c < (b-a):
        print("advertise")
    else:
        print("do not advertise")
