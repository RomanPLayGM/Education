
n = int(input())
m = int(input())
if n > m:
    print(m * 2)
else:
    print((n * 2) - 1)
print(min(2 * n - 1, 2 * m))
