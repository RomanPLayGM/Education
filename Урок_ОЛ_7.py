"""Определим близость двух строк следующим образом: выделим у обоих строк наибольший общий префикс (совпадающие буквы
в начале строк) и удалим его. Затем выделим наибольший общий суффикс у обеих строк (совпадающие буквы в конце строк)
и тоже удалим его. Сумма длин удалённого префикса и суффикса будет равна близости этих строк. К примеру,
близость строк programming и pruning равна пяти: cначала удаляем наибольший общий префикс pr, затем удаляем
наибольший общий суффикс ing. Сумма длин этих строк равна 2+3 = 5. Также близость строк hse и hsehsehse равна трём,
поскольку после удаления наибольшего общего префикса hse, длина наибольшего общего суффикса у пустой строки и hsehse
равна нулю. Дан набор из n строк. Для каждой строки найдите ближайшую к ней из набора, исключая саму эту строку.

Формат входных данных Первая строка входных данных содержит одно целое число n > 2 — число строк. Каждая из следующих
n строк содержат одну строку из строчных букв латинского алфавита.

Формат выходных данных В единственной строке
выходных данных выведите n чисел, разделённых пробелом — номера ближайших строк для каждой строки. Строки
пронумерованы от 1 до n в том порядке, в котором они перечисляются во входном файле. Если возможных ответов
несколько, выведите любой из них.
"""


def closeness_of_two_lines(line_1, line_2):
    min_len_line = min(line_1, line_2, key=len)
    result = 0
    for symbol in range(len(min_len_line)):
        if line_1[symbol] == line_2[symbol]:
            result += 1
        else:
            break
    for symbol in range(len(min_len_line)):
        if line_1[-(symbol + 1)] == line_2[-(symbol + 1)]:
            result += 1
        else:
            break
    if result > len(min_len_line):
        result = len(min_len_line)
    return result


n = int(input())
list_string = [input() for i in range(n)]
for number_line in range(len(list_string)):
    line = list_string[number_line]
    closeness = 0
    max_number_line = 0
    for number_check_line in range(len(list_string)):
        if number_line != number_check_line and closeness < len(list_string[number_check_line]):
            check_line = list_string[number_check_line]
            closeness_value = closeness_of_two_lines(line, check_line)
            if closeness <= closeness_value:
                closeness = closeness_value
                max_number_line = number_check_line + 1
    print(max_number_line, end=" ")
