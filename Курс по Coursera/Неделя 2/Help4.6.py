max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
n = int(input())
while n != 0:
    if max1 < n:
        max2, max1 = max1, n
    elif max2 < n:
        max2 = n
    n = int(input())
print(max2)
