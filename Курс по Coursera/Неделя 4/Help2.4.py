def gcd(a, b):
    if a % b == 0:
        return b
    if b % a == 0:
        return a
    else:
        return gcd(b, a % b)


a1, b1 = float(input()), float(input())
print(int(gcd(a1, b1)))
