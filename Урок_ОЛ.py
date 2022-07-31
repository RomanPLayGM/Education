
def fact_help(a, acc1, acc2, sum_0):
    if a == 1:
        return sum_0 + 1
    return fact_help(a - 1, acc2, acc1 + acc2, acc1 + acc2 + sum_0)


def fact(a):
    return fact_help(a, 0, 1, 0)


def perimeter(number_squares):
    number_squares_1 = number_squares + 1
    return 4 * (fact(number_squares_1))


print(perimeter(7))
