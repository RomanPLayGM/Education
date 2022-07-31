def power(a, n):
    i = 1
    b = a
    if n == 1:
        return a
    elif n == 0:
        return 1
    elif n < 0:
        while i < abs(n):
            i += 1
            b *= a
        return 1 / b
    while i < n:
        i += 1
        b *= a
    return b


a1, n1 = float(input()), float(input())
print(power(a1, n1))
