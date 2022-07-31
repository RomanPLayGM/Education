x = int(input())
y = int(input())
xy = x * 60 + y
print(xy)
xy = xy % (24 * 60 * 60)
print(xy)
h = xy // 3600
print(h)