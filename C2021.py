n, m = map(int, input().split())
m1 = []
m2 = []
k1 = 0
for i in range(m):
    l, r, k = map(int, input().split())
    for j in range(l, r + 1):
        m1.append(j)
    for u in m1:
        if k == 2:
            if u % 2 == 0:
                k1 += 1
        else:
            k1 = len(m1)
            break
    m1 = []
    m2.append(k1)
    k1 = 0
print(int((sum(m2)) / n))