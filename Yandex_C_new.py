from time import perf_counter
start = perf_counter()
# n, m = input().split()
# n, m = int(n), int(m)
n, m = 5, 3
# a = list(map(int, input().split()))
a = [7, 3, 4, 2, 2]
# b = list(map(int, input().split()))
b = [3, 2, 1]
b.sort()
d = {}
# d = {0: 1, 1: 2, 2: 3}
# d = {i: j for i, j in enumerate(b)}
for i in range(0, len(b)):
    d[i] = b[i]
m1 = list()
for i in range(0, len(a)):
    try:
        a1 = max(a[i + 1:])
        if a[i] - a1 > 0:
            m1.append(a[i] - a1)
    except ValueError:
        m1.append(a[i])
m1.sort()
k = 0
j = 0
i = 0
# m2 = {0: 2, 1: 2, 2: 3}
while i < len(d) and j < len(m1):
    if m1[j] >= d[i]:
        k += 1
        i += 1
        j += 1
    else:
        j += 1
end = perf_counter()
print(end - start)
