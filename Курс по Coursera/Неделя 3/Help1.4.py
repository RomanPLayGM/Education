import math
n = float(input())
e = (n - math.floor(n))
e1 = math.floor(n)
if e >= 0.50:
    e1 += 1
    print(e1)
else:
    print(e1)
