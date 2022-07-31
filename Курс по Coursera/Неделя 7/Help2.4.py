n, k = map(int, input().split())
ls = set()
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, n + 1, b):
        if j not in ls and (j - 6) % 7 != 0 and j % 7 != 0:
            ls.add(j)
print(len(ls))
