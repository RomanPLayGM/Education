def revers():
    n = int(input())
    if n != 0:
        revers()
    print(n)


revers()
