def summ():
    n = int(input())
    if n != 0:
        n += summ()
    return n


print(summ())
