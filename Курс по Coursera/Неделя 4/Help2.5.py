def ReduceFraction(n, m):
    if n % m == 0:
        return m
    if m % n == 0:
        return n
    else:
        return ReduceFraction(m, n % m)


a1, b1 = float(input()), float(input())
y = ReduceFraction(a1, b1)
print(int(a1 / y), int(b1 / y))
