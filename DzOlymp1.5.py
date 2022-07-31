n = int(input())
k = 1
if (n - 1) == 0:
    print(9)
else:
    while (n - 1) != 0:
        k *= 10
        n -= 1
    print(9 * k)