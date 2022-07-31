n = int(input())
max1 = n
k = 0
while n != 0:
    if max1 < n:
        max1 = n
        k = 0
    if n == max1:
        k += 1
    n = int(input())
print(k)
