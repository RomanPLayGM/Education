n, m = input().split()
n, m = int(n), int(m)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m1 = list()
for i in range(0, len(a)):
    try:
        a1 = max(a[i + 1:])
        if a[i] - a1 > 0:
            m1.append(a[i] - a1)
    except ValueError:
        m1.append(a[i])
m1.sort()
b.sort()
k = 0
j = 0
i = 0
while i < len(b) and j < len(m1):
    if m1[j] >= b[i]:
        k += 1
    else:
        i -= 1
    i += 1
    j += 1
print(k)
