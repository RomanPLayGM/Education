def add_tuple(my_tuple, key, a):
    if my_tuple.get(key, -1) == -1:
        my_tuple[key] = (a,)
    else:
        my_tuple[key] = my_tuple[key] + (a,)


def help_picture(picture1, key1, j1, sp=True):
    if sp:
        picture1[j1][key1] = 2
    else:
        picture1[key1][j1] = 2


def add_picture(my_dict, reverse=True):
    # key - значение y_i в picture
    for key in my_dict:
        for i in range(0, len(my_dict[key]), 2):
            # j - значение x_i в picture
            step = -1 if my_dict[key][i] > my_dict[key][i + 1] else 1
            for j in range(my_dict[key][i] + step, my_dict[key][i + 1], step):  # если (2, 6) -> хотим получить 3, 4, 5
                help_picture(picture, key, j, reverse)


def cells(pic):
    min_x = []
    max_x = []
    k1 = 0
    k2 = 0
    for i in range(len(pic[k2])):
        k2 += 1
        for j in range(len(pic)):
            if pic[j][i] == 2 or pic[j][i] == 1:
                min_x.append(j)
                break
        for j1 in range(len(pic) - 1, 0, -1):
            if pic[j1][i] == 2:
                max_x.append(j1)
                break
        k1 += 1
    return [min_x] + [max_x]


def syu(pic):
    for i in range(1, len(pic) - 1):
        flag = True
        for j in range(1, len(pic[0]) - 1):
            if flag:
                if pic[i][j] == 1 or pic[i][j] == 2:
                    flag = True
                    continue
                else:
                    flag = False
            else:
                pic[i][j] = 3
                continue
    return False


def full_cells(pic, arr, count):
    k5 = 0
    for i in range(len(pic[0])):
        for j in range(arr[0][k5], arr[1][k5]):
            if pic[j][i] == 0:
                # print("i:", i, "j:", j)
                # pic[j][i] = 3
                count += 1
        k5 += 1
    return count


def half_cells(pic):
    sum_2 = 0
    for i in pic:
        sum_2 += i.count(2)
    return sum_2


def internal_corners1(pic):
    count_internal_corners = 0
    count_outside_corners = 0
    for i in range(len(pic)):
        if i == 0:
            for j in range(len(pic[0])):
                if j == 0:
                    if pic[i][j] == 1:
                        if (pic[1][0] == 2 and pic[0][1] == 2) or (pic[1][0] == 1 and pic[0][1] == 2) or (pic[1][0] == 2 and pic[0][1] == 1):
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
                elif j == len(pic[0]) - 1:
                    if pic[i][j] == 1:
                        if (pic[0][len(pic[0]) - 2] == 2 and pic[1][len(pic[0]) - 1] == 2) or (pic[0][len(pic[0]) - 2] == 1 and pic[1][len(pic[0]) - 1] == 2) or (pic[0][len(pic[0]) - 2] == 2 and pic[1][len(pic[0]) - 1] == 1):
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
                else:
                    if pic[i][j] == 1:
                        if pic[i][j - 1] == 0 or pic[i][j + 1] == 0:
                            count_outside_corners += 1
                        elif pic[i][j - 1] == 1 and pic[i][j + 1] == 1:
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
        elif i == len(pic) - 1:
            for j in range(len(pic[-1])):
                if j == 0:
                    if pic[i][j] == 1:
                        if (pic[len(pic) - 2][0] == 2 and pic[len(pic) - 1][1] == 2) or (pic[len(pic) - 2][0] == 1 and pic[len(pic) - 1][1] == 2) or (pic[len(pic) - 2][0] == 2 and pic[len(pic) - 1][1] == 1):
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
                elif j == len(pic[-1]) - 1:
                    if pic[i][j] == 1:
                        if (pic[len(pic) - 2][len(pic[len(pic) - 2]) - 1] == 2 and pic[len(pic[-1]) - 1][len(pic[-1]) - 2] == 2) or (pic[len(pic) - 2][len(pic[len(pic) - 2]) - 1] == 1 and pic[len(pic[-1]) - 1][len(pic[-1]) - 2] == 2) or (pic[len(pic) - 2][len(pic[len(pic) - 2]) - 1] == 2 and pic[len(pic[-1]) - 1][len(pic[-1]) - 2] == 1):
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
                else:
                    if pic[i][j] == 1:
                        if pic[i][j - 1] == 0 or pic[i][j + 1] == 0:
                            count_outside_corners += 1
                        elif pic[i][j - 1] == 1 and pic[i][j + 1] == 1:
                            count_outside_corners += 1
                        else:
                            count_internal_corners += 1
        else:
            if i < len(pic[i]) / 2:
                for j in range(len(pic[i])):
                    if j == 0:
                        if pic[i][j] == 1:
                            if pic[i - 1][j] == 0 or pic[i + 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
                    elif j == len(pic[i]) - 1:
                        if pic[i][j] == 1:
                            if pic[i - 1][j] == 0 or pic[i + 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
                    else:
                        if pic[i][j] == 1:
                            if pic[i - 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
            else:
                for j in range(len(pic[i])):
                    if j == 0:
                        if pic[i][j] == 1:
                            if pic[i - 1][j] == 0 or pic[i + 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
                    elif j == len(pic[i]) - 1:
                        if pic[i][j] == 1:
                            if pic[i - 1][j] == 0 or pic[i + 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
                    else:
                        if pic[i][j] == 1:
                            if pic[i + 1][j] == 0:
                                count_outside_corners += 1
                            else:
                                count_internal_corners += 1
    return str(count_outside_corners) + " " + str(count_internal_corners)


n, m = map(int, input().split())
k = int(input())
x = {}
y = {}
picture = [[0] * n for i in range(m)]
for i in range(k):
    x_i, y_i = map(lambda t: int(t) - 1, input().split())
    add_tuple(x, x_i, y_i)
    add_tuple(y, y_i, x_i)
    picture[y_i][x_i] = 1
# picture.reverse()
# print('x:', x)  # вертикальные
# print('y:', y)  # горизонтальные
# key - значение y_i в picture
add_picture(x)
add_picture(y, False)
# array_cells = cells(picture)
# print(array_cells)
# print(*picture[::-1], sep='\n')
# print(full_cells(picture, array_cells, 0))
# internal_corners1(picture)
# print(half_cells(picture))
syu(picture)
# print(full_cells(picture, array_cells, 0), half_cells(picture), internal_corners1(picture))
print(*picture[::-1], sep='\n')
