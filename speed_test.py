"""
Скорость работы различных алгоритмических конструкций
"""
import random
from timeit import timeit


# # # # # # # # # # # # # # Фильтрация None значений # # # # # # # # # # # # # # # # #

# # filter(lambda)
# def filter_lambda(x):
#     return list(filter(lambda z: z, x))
#
#
# # filter(None)
# def filter_none(x):
#     return list(filter(None, x))
#
#
# # filter(bool)
# def filter_bool(x):
#     return list(filter(bool, x))
#
#
# # list comprehension [i for i in a if i]
# def list_comprehension(x):
#     return [i for i in x if i]
#
#
# # for
# def for_(x):
#     res = []
#     for i in x:
#         if i:
#             res.append(i)
#     return res
#
#
# # while
# def while_(x):
#     i = 0
#     res = []
#     while i < len(x):
#         if x[i]:
#             res.append(x[i])
#         i += 1
#     return res
#
#
# def main(x, number=1000):
#     print('filter_lambda:', timeit(f'filter_lambda({x})', number=number, globals=globals()))
#     print('filter_none:', timeit(f'filter_none({x})', number=number, globals=globals()))
#     print('filter_bool:', timeit(f'filter_bool({x})', number=number, globals=globals()))
#     print('list_comprehension:', timeit(f'list_comprehension({x})', number=number, globals=globals()))
#     print('for_:', timeit(f'for_({x})', number=number, globals=globals()))
#     print('while_:', timeit(f'while_({x})', number=number, globals=globals()))
#
#
# a = [None, 1, 0, '', 5, {'qwe': 'asd'}, [55, 66], [], set(), False, True] * 3000
# b = [354, -1, None, 0, 44, 5, -2999, None] * 3000
# main(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # Фильтрация значений > 10 # # # # # # # # # # # # # # # # #

# # filter(lambda)
# def filter_lambda(x):
#     return list(filter(lambda z: z > 10, x))
#
#
# # filter(func)
# def filter_func(x):
#     def _gt(z):
#         return z > 10
#     return list(filter(_gt, x))
#
#
# # list comprehension [i for i in a if i]
# def list_comprehension(x):
#     return [i for i in x if i > 10]
#
#
# # for
# def for_(x):
#     res = []
#     for i in x:
#         if i > 10:
#             res.append(i)
#     return res
#
#
# # while
# def while_(x):
#     i = 0
#     res = []
#     while i < len(x):
#         if x[i] > 10:
#             res.append(x[i])
#         i += 1
#     return res
#
#
# def main(x, number=1000):
#     print('filter_lambda:', timeit(f'filter_lambda({x})', number=number, globals=globals()))
#     print('filter_func:', timeit(f'filter_func({x})', number=number, globals=globals()))
#     print('list_comprehension:', timeit(f'list_comprehension({x})', number=number, globals=globals()))
#     print('for_:', timeit(f'for_({x})', number=number, globals=globals()))
#     print('while_:', timeit(f'while_({x})', number=number, globals=globals()))
#
#
# a = [354, -1, 0, 0, 44, 5, -2999, 0] * 3000
# main(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # Изменение значений в iterable # # # # # # # # # # # # # # #

# # map(lambda)
# def map_lambda(x):
#     return list(map(lambda z: z.lower() if z else '', x))
#
#
# # map(func)
# def map_func(x):
#     def _lower(z):
#         return z.lower() if z else ''
#     return list(map(_lower, x))
#
#
# # list comprehension
# def list_comprehension(x):
#     return [i.lower() if i else '' for i in x]
#
#
# # for
# def for_(x):
#     res = []
#     for i in x:
#         res.append(i.lower() if i else '')
#     return res
#
#
# # while
# def while_(x):
#     res = []
#     i = 0
#     while i < len(x):
#         res.append(x[i].lower() if x[i] else '')
#         i += 1
#     return res
#
#
# def main(x, number=1000):
#     print('map_lambda:', timeit(f'map_lambda({x})', number=number, globals=globals()))
#     print('map_func:', timeit(f'map_func({x})', number=number, globals=globals()))
#     print('list_comprehension:', timeit(f'list_comprehension({x})', number=number, globals=globals()))
#     print('for_:', timeit(f'for_({x})', number=number, globals=globals()))
#     print('while_:', timeit(f'while_({x})', number=number, globals=globals()))
#
#
# a = ['ASasdmxzcs', 'ASDADDDD', 'JsAdppEewq', None, 'zxc', None] * 3000
# main(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # Сортировка # # # # # # # # # # # # # # # # # # # #


# sort
def sort_(x):
    return x.sort()


# sorted
def sorted_(x):
    return sorted(x)


# Быстрая сортировка Хоара
def quicksort(x):
    if len(x) <= 1:
        return x
    else:
        q = random.choice(x)
    l_nums = [n for n in x if n < q]

    e_nums = [q] * x.count(q)
    b_nums = [n for n in x if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


# Пузырьковая сортировка
def bubble(x):
    n = 1
    while n < len(x):
        for i in range(len(x) - n):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
        n += 1
    return x


def main(x, number=1000):
    print('sort_:', timeit(f'sort_({x.copy()})', number=number, globals=globals()))
    print('sorted_:', timeit(f'sorted_({x})', number=number, globals=globals()))
    print('quicksort:', timeit(f'quicksort({x})', number=number, globals=globals()))
    print('bubble:', timeit(f'bubble({x.copy()})', number=number, globals=globals()))


a = [1, -5, 3, -100, 10, 2, 44444, 100, -343, 3, 6, 1111, 0, 0] * 3000
main(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
