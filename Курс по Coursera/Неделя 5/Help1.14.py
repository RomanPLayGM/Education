n = list(map(int, input().split()))
maximum = max(n)
minimum = min(n)
maxpos = n.index(maximum)
minpos = n.index(minimum)
n[maxpos], n[minpos] = n[minpos], n[maxpos]
print(*n)
