def IsPrime(n):
    if n < 2:
        return False
    else:
        if n % 2 == 0 and n != 2:
            return False
        else:
            if n == 2:
                return True
            else:
                k = 2
                while k <= (n ** 0.5):
                    if n % k == 0:
                        return False
                    k += 1
                return True


n1 = int(input())
if IsPrime(n1):
    print("YES")
else:
    print("NO")
