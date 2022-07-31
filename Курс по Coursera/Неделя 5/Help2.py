a = list(map(int, input().split()))
b = list()
c = list()
b.append(max(a))
c.append(min(a))
a.remove(max(a))
a.remove(min(a))
b.append(max(a))
c.append(min(a))
if b[0] * b[1] >= c[0] * c[1]:
    print(*(min(b), max(b)))
else:
    print(*(min(c), max(c)))
