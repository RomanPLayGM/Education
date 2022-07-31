n, m = map(int, input().split())
k = int(input())
m1 = []
m2 = []
m1_1 = []
m2_1 = []
x1 = {}
y1 = {}
for i in range(m):
    for j in range(n):
        m2.append(0)
    m1.append(m2)
    m2 = []
for i in range(n):
    for j in range(m):
        m2_1.append(0)
    m1_1.append(m2_1)
    m2_1 = []
#print(m1)
#print(m1_1)
for i in range(k):
    x, y = map(int, input().split())
    m1[y - 1][x - 1] = 1
    m1_1[x - 1][y - 1] = 1
#print(m1)
#print(m1_1)
k = 0
k2 = 0
m1_new = []
m4 = []
for y in range(len(m1)):
    m4 = list(reversed(m1[y]))
    for j in range(len(m4)):
        if m4[j] == 1:
            k = j
            break
    k1 = len(m1[y]) - k - 1
    for i in range(len(m1[y])):
        if m1[y][i] == 1:
            k2 = i
            break
    m1_new = m1[y][k2:k1 + 1]
    if m1_new.count(1) > 0:
        for u in range(k2, k1 + 1):
            m1[y][u] = 1
    k1 = 0
    k2 = 0
k = 0
k2 = 0
m1_new = []
m4 = []
for y in range(len(m1_1)):
    m4 = list(reversed(m1_1[y]))
    for j in range(len(m4)):
        if m4[j] == 1:
            k = j
            break
    k1 = len(m1_1[y]) - k - 1
    for i in range(len(m1_1[y])):
        if m1_1[y][i] == 1:
            k2 = i
            break
    m1_new = m1_1[y][k2:k1 + 1]
    if m1_new.count(1) > 0:
        for u in range(k2, k1 + 1):
            m1_1[y][u] = 1
    k1 = 0
    k2 = 0
print(m1)
print(m1_1)
#m3 = m1[y][i:]
#print("y", m1)
#print("x", m1_1)
for i in range(len(m1_1)):
    for j in range(len(m1_1)):
        if m1_1[i][j] == 1:
            m1[j][i] = m1_1[i][j]
for i in list(reversed(m1)):
    print(i)
k = 0
k2 = 0
m1_new = []
m4 = []
for y in range(len(m1)):
    m4 = list(reversed(m1[y]))
    k2 = m1[y].index(1)
    k = len(m1[y]) - m4.index(1) - 1
    m1_new = m1[y][k2 + 1:k]
    if len(m1_new) > 1:
        if m1_new[0] == 0 or m1_new[-1] == 0:
            k1 = 0
            m5 = list(reversed(m1_new))
            while m1_new[k1] != 1:
                m1[y][k1 + 1] = 1
                k1 += 1
            k1 = 0
            while m5[k1] != 1:
                m1[y][len(m1_new) - k1] = 1
                k1 += 1
        else:
            continue
