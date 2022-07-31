def phib(n):
    if n < 2:
        return n
    return phib(n - 1) + phib(n - 2)


n1 = int(input())
print(phib(n1))
