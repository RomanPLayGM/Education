def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


a1, n1 = float(input()), float(input())
print(power(a1, n1))
