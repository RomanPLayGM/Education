a = int(input())
b = int(input())
a1 = str(a)
b1 = str(b)
c = a - b
c1 = (b - a)
a5 = a1*0**abs(c - abs(c1)) + b1*0**abs(c1 - abs(c))
a7 = len(a1*0**abs(c - abs(c1)))
a8 = len(b1*0**abs(c1 - abs(c)))
a9 = len(a1*0**abs(c - abs(c1)))
a6 = a5[:abs(a7 - a8) + a9]
print(a6)
