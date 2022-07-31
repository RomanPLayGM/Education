a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print("INF")
    exit()
if a == 0 and c != 0:
    print("INF")
    exit()
if a != 0 and c == 0:
    print(- b // a)
    exit()
if c == 0 and d == 0:
    print("NO")
    exit()
if b == 0:
    print("NO")
    exit()
if a != 0 and c != 0 and b % a == 0:
    a1 = -b / a
    a2 = -(b // a)
    b1 = -d / c
    if a1 - a2 == 0:
        if a1 != b1:
            print(int(a1))
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
