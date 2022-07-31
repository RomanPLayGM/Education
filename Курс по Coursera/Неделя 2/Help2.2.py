a = int(input())
b = int(input())
c = int(input())
a1 = a ** 2 + b ** 2
b1 = c ** 2 + b ** 2
c1 = a ** 2 + c ** 2
p = (a + b + c) / 2
if a == 0 or b == 0 or c == 0:
    print("impossible")
    exit()
if (p * (p - a) * (p - b) * (p - c)) ** 0.5 == 0:
    print("impossible")
    exit()
if (a + b >= c) and (a + c >= b) and (b + c >= a):
    if (a >= b) and (a >= c):
        if b1 == a ** 2:
            print("rectangular")
        elif b1 >= a ** 2:
            print("acute")
        elif b1 <= a ** 2:
            print("obtuse")
    elif (b >= a) and (b >= c):
        if c1 == b ** 2:
            print("rectangular")
        elif c1 >= b ** 2:
            print("acute")
        elif c1 <= b ** 2:
            print("obtuse")
    elif (c >= a) and (c >= b):
        if a1 == c ** 2:
            print("rectangular")
        elif a1 >= c ** 2:
            print("acute")
        elif a1 <= c ** 2:
            print("obtuse")
else:
    print("impossible")
