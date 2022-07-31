def get(x1, y1, dict1):
    if dict1.get(x1):
        dict1[x1] += (y1,)
    else:
        dict1[x1] = (y1,)
    return dict1


# def sum_relative(relative, dict_relative):
#     for relative_x_or_y in dict_relative:
#         relative += sum(dict_relative[relative_x_or_y])
#     return relative
def sum_relative(relative, dict_relative):
    len_dict = 0
    for relative_first in dict_relative:
        relative += sum(dict_relative[relative_first])
        len_dict += len(dict_relative[relative_first])
    relative /= len_dict
    for relative_x_y in dict_relative:
        sorted_dict = sorted(dict_relative[relative_x_y])
        for extreme in range(len(sorted_dict)):
            secondary_relative = (sorted_dict[extreme] + sorted_dict[-1 * extreme - 1]) / 2
            if secondary_relative != relative:
                return
    return relative


# def relative_axis(sum_relative_x_or_y, count):
#     if count == 0 and not sum_relative_x_or_y:
#         print("По оси x")
#     elif not sum_relative_x_or_y:
#         print("По оси y")
#     else:
#         print("Нет")
def relative_axis(relative_x_1, relative_y_1):
    if relative_x_1 is None and relative_y_1 is not None:
        print("По оси Y: x =", relative_y_1)
    elif relative_x_1 is None and relative_y_1 is None:
        print("Нет такой оси")
    else:
        print("По оси X: y =", relative_x_1)


n = int(input())
dict_x = {}
dict_y = {}
for i in range(n):
    x, y = map(int, input().split())
    get(x, y, dict_x)
    get(y, x, dict_y)
relative_x = sum_relative(0, dict_x)
relative_y = sum_relative(0, dict_y)
relative_axis(relative_x, relative_y)
# relative_x = 0
# relative_y = 0
# relative_axis(sum_relative(relative_x, dict_x), 0)
# relative_axis(sum_relative(relative_y, dict_y), 1)
