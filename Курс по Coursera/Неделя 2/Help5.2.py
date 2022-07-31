n = int(input())
k = 1
count = 0
while k <= n:
    k1 = 0
    s1 = ''
    while (k // 10 ** k1) != 0:
        s = (k // 10 ** k1) % 10
        k1 += 1
        s1 = int(str(s1) + str(s))
    if s1 == k:
        count += 1
    k += 1
print(count)
