c1 = a1 = b1 = int(input())
n = n1 = n2 = n3 = 0
while c1 != 0:
    if a1 < b1 > c1:
        n2 = n1
        if n3 > n2:
            n3 = n2
        n1 = 1
        n += 1
    else:
        n1 += 1
    if n == 2:
        n3 = n2
    a1 = b1
    b1 = c1
    c1 = int(input())
print(n3)
