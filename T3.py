print(2 ** 32 - (2 ** 31) + (2 ** 30) - ((2 ** 30 + 2) / 3))
print((2 ** 30 + 2) / 3)
k = 0
for i in range(32, 0, -1):
    if i % 2 == 0:
        k += 2 ** i
    else:
        k -= 2 ** i
print(k)
