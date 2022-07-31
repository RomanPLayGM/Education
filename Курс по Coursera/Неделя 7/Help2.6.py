s = int(input())
d = {}
k = 0
for i in range(s):
    k = list(input().split())
    for j in range(1, len(k)):
        d[k[j]] = k[0]
m = int(input())
m1 = list()
for i in range(m):
    m1.append(d.get(input()))
for i in m1:
    print(i)
