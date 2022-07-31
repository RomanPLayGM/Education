n = int(input())
k = 0
s = 0
# или с помощью формулы n*(n + 1)*(2n + 1)/6
while n >= k:
    s += k ** 2
    k += 1
print(s)
