p = int(input())
p1 = p * 0.08
p2 = p * 0.05
if p1 > p2:
    if p1 < 100:
        print(p1)
    else:
        print(100)
else:
    print(p2)
