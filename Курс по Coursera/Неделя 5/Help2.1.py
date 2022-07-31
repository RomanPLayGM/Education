a = list(map(int, input().split()))
x = a.pop(a.index(max(a)))
y = a.pop(a.index(max(a)))
z = max(a)
a.append(x)
a.append(y)
x1 = a.pop(a.index(min(a)))
y1 = a.pop(a.index(min(a)))
z1 = min(a)
res = x * y * z
res1 = (x1 * y1 * z1)
res2 = (x1 * y1 * x)
if res >= res1 and res >= res2:
    print(y, x, z)
elif res1 >= res2 and res1 >= res:
    print(x1, y1, z1)
elif res2 >= res1 and res2 >= res:
    print(x1, y1, x)
