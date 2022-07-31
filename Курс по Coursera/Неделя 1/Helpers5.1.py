n = int(input())
n *= 60
n = n % (24 * 60 * 60)
h = n // (60 * 60)
n = n % (60 * 60)
m = n // 60
print(h, m)
