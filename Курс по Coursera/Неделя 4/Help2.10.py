def revers(flag=0):
    n = int(input())
    if n != 0:
        if revers():
            flag = 1
        if (n ** 0.5 % 1) == 0.0 and n != 0:
            flag = 1
            print(n, end=" ")
    return flag


if revers() == 0:
    print("0")
