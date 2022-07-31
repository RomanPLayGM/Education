n, k, n1, k1 = map(int, input().split())
if ((n == 1 and n1 == 4) or (n == 4 and n1 == 1)) or ((n == 2 and n1 == 5) or (n == 5 and n1 == 2)) or ((n == 3 and n1 == 6) or (n == 6 and n1 == 3)):
    print(k + k1)
elif n == n1:
    if k < k1:
        print(k1 - k)
    else:
        print(k - k1)
else:
    if n < n1:
        if ((n1 - n) == 1) or ((n1 - n) == 3) or ((n1 - n) == 5):
            print(max(k, k1))
        else:
            print(k + k1)
    else:
        if ((n - n1) == 1) or ((n - n1) == 3) or ((n - n1) == 5):
            print(max(k, k1))
        else:
            print(k + k1)






