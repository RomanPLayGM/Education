def C(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    if k == 0:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)


n1, k1 = int(input()), int(input())
print(C(n1, k1))
