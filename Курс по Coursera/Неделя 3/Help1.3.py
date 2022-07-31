import math
n = float(input())
e = round((n - math.floor(n)) * 100)
e1 = math.floor(n)
print(e1, e)
