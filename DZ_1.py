# def decorator_decorator(a, b):
#     def decorator(func):
#         def wrapper(*args):
#             return func(*args[:-1]) * args[-1] + a + b
#
#         return wrapper
#     return decorator
#
# @decorator_decorator(100, 1000)
# def my_sum(*args):
#     print(args, type(args))
#     x = 0
#     for i in args:
#         x += i
#     return x
#
#
# print(my_sum(10, 5, 3))

def super_sum(x):
    result = x

    def sum_m(y=None):
        nonlocal result
        if y is None:
            return result
        else:
            result += y
            return sum_m

    return sum_m


print(super_sum(5)(10)(15)())
