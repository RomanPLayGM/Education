n = int(input())
k = 0
k1 = 0
m = n
while m != 0:
    m //= 10
    k += 1
while k > k1:
    s = (n // 10 ** k1) % 10
    k1 += 1
    print(s, end="")
