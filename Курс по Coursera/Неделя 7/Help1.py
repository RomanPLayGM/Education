a = list(map(int, input().split()))
a = sorted(a)
n = 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        n += 1
print(n)
