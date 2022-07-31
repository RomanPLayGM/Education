k, m, n, = (int(input()), int(input()), int(input()))
if 2 * n % k == 0 and n > k:
    print((n * 2 // k) * m)
else:
    if n % k != 0 and k < n:
        print((n * 2 // k) * m + m)
    else:
        if n <= k:
            print(2 * m)


k = int(input())
m = int(input())
n = int(input())
if k == 0 or m == 0 or n == 0:
    print(0)
    exit()
t = abs(n) // abs(k)
t1 = abs(n) % abs(k)
if abs(n) >= abs(k):
    if abs(n) - abs(k) == 1 or t1 == 1:
        print((t * abs(m) * 2) + ((abs(n) % abs(k)) * abs(m)))
    else:
        if abs(k) != 1:
            if abs(n) % abs(k) == 0:
                print((abs(n) // abs(k)) * abs(m) * 2)
            else:
                if abs(n) % abs(k) > (k / 2):
                    print(1)
                    print((t * abs(m) * 2) + (abs(m) * 2))
                else:
                    print(2)
                    print(t * abs(m) * 2 + abs(m))
        else:
            print(abs(n) * abs(m) * 2)
else:
    print(abs(m) * 2)