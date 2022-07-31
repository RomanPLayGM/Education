a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - b * c
delta_a = e * d - f * b
delta_b = a * f - e * c
a1 = delta_a / delta
b1 = delta_b / delta
print(a1, b1)
