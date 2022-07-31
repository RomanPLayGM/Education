a = list(map(int, input().split()))
max1 = a[1]
j = 0
for i in range(len(a)):
    if a[i] >= max1:
        max1 = a[i]
        j = i
print(max1, j)
