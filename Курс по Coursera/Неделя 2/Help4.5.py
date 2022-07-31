n = int(input())
s = n
k = 0
while n != 0:
    n = int(input())
    if s < n:
        k += 1
    s = n
print(k)
