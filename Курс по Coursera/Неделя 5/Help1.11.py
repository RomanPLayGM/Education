m = list(map(int, input().split()))
for i in range(len(m)):
    if m[i] <= 0:
        m[i] = max(m) + 1
print(min(m))
