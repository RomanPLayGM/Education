n = int(input())
fib0 = 0
fib1 = 1
k = 1
while fib1 < n:
    k += 1
    fib1, fib0 = fib0 + fib1, fib1
if fib1 != n:
    k = -1
if n == 0:
    print(0)
else:
    print(k)
