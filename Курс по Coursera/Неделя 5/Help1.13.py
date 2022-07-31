x = list(map(str, input().split()))
y = 0
while len(x) > y + 1:
    x[y], x[y + 1] = x[y + 1], x[y]
    y += 2
print(" ".join(x))
