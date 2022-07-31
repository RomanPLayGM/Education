def nod(n):
    k = 2
    while k <= int(n ** 0.5):
        if n % k == 0:
            return k
        k += 1
    return n


n1 = int(input())
print(nod(n1))
