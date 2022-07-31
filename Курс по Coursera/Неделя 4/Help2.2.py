def sum1(a, b):
    if b > 0:
        return sum1(a + 1, b - 1)
    else:
        return a


a1, b1 = int(input()), int(input())
print(sum1(a1, b1))
