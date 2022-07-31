n = int(input())
m = int(input())
n1 = n
m1 = m
k = 1
const1 = 0
while n > 0:
    n -= k
    m += k
    k += 1
    const1 += 1
    if n > 0:
        n += k
        m -= k
        k += 1
        const1 += 1
    else:
        break
k = 1
const2 = 0
while m1 > 0:
    n1 -= k
    m1 += k
    k += 1
    const2 += 1
    if m1 > 0: # !=
        n1 += k
        m1 -= k
        k += 1
        const2 += 1
    else:
        break
print(min(const1, const2))