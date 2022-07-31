n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in range(max(n, m)):
    if i < n:
        a[i] = [a[i], i]
    if i < m:
        b[i] = [b[i], i + 1]
a.sort(), b.sort()
print(a)
print(b)
j, k = 0, 0
while j < len(a):
    if k + 1 < len(b):
        if abs(a[j][0] - b[k][0]) <= abs(a[j][0] - b[k + 1][0]):
            a[j].append(b[k][1])
            j += 1
        else:
            k += 1
    else:
        a[j].append(b[k][1])
        j += 1
print(a)
a.sort(key=lambda x: x[1])
print(a)
for i1 in range(len(a)):
    print(a[i1][2], end=' ')
