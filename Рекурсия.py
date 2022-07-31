# def fact_help(a, acc):
    # if a == 2:
        # return acc
    # return fact_help(a - 1, acc * (a - 1))

# def fact(a):
    # return fact_help(a, a)

# x = 5
# print(fact(x))
x = [1, 2, 3, 4]
for i in x:
    if i == 3:
        print("YES")

if 5 in x:  # БЫСТРЕЕ ЧЕМ
    print("YES")


a = str(bin(8 ** 1023 + 2 ** 1024 - 3))
k = 0
for i in a:
    if i == "1":
        k += 1
print(k)

def fib_help(a, acc):
    fib0 = 1
    if a > 1:
        return fib_help(a - 1, acc) + fib_help(a - 2, fib0)
    else:
        return fib0


def fib1(a):
    return fib_help(a - 1, 0)


print(fib1(43))


def fib(a):
    if a < 2:
        return a
    return fib(a - 1) + fib(a - 2)


print(fib(43))


def fib_help2(acc1, acc, a):
    if a > 0:
        return fib_help2(acc, acc + acc1, a - 1)
    else:
        return acc1



def fib2(a):
    return fib_help2(0, 1, a)


print(fib2(43))


def fib(a):
    if a < 2:
        return a
    return fib(a - 1) + fib(a - 2)


print(fib(50))



