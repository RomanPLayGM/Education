n = int(input())
k = 1
k1 = 0
while n >= k:
    k *= 2
    k1 += 1
if k % n == 0:
    k1 -= 1
print(k1)
