"""
У Валеры есть мультимножество неотрицательных целых чисел размера n и q запросов на изменение этого
мультимножества. Мультимножество может содержать несколько одинаковых элементов. Запросы бывают трёх типов: 1.
Прибавить 1 ко всем числам в мультимножестве. 2. Добавить число в мультимножество. 3. Удалить один экземпляр значения
из мультимножества (если таких чисел в мультимножестве нет, ничего делать не нужно). Валера - большой поклонник
битовых операций, в особенности операции побитового исключающего или (xor). Ему очень хочется узнать каким был
результат выполнения операции xor для всех элементов мультимножества после каждого изменения. В программировании
Валера не очень силён, поэтому решить эту задачу предстоит вам.
Формат входных данных:
В первой строке вводятся два
целых числа n, q (1 6 n, q 6 200 000) — размер массива a и количество запросов. Во второй строке вводится n целых
чисел a1, a2,..., an (0 6 ai 6 1018) — изначальное мультимножество чисел Валеры. В следующих q строках будет
информация о запросах по одному на строке. Каждая из них будет начинаться с числа type_i (1 6 type_i 6 3) — типа
запроса. Если это запрос второго, или третьего типа, через пробел после типа будет число value_i (0 6 value_i 6 1018)
— значение, которое нужно добавить в мультимножество, если type_i = 2 и удалить, если type_i = 3.
Формат выходных:
данных: В i-й строке выведите результат выполнения операции xor для всех чисел в мультимножестве Валеры после первых
i изменений.

Пример входных данных:
5 5
0 1 3 4 4
1
2 0
1
3 7
3 6

Пример выходных данных:
7
7
5
5
3
"""
from functools import reduce


class Multiset:
    def __init__(self, line):
        self.multiset = self._prepare(line)

    @staticmethod
    def _prepare(line):
        multiset = {}
        for value in line.split():
            value_int = int(value)
            if multiset.get(value_int):
                multiset[value_int] += 1
            else:
                multiset[value_int] = 1
        return multiset

    def plus_one(self, _a):
        self.multiset = {key + 1: self.multiset[key] for key in self.multiset}

    def add_key(self, new_key):
        new_key = int(new_key)
        if self.multiset.get(new_key):
            self.multiset[new_key] += 1
        else:
            self.multiset[new_key] = 1

    def minus_one(self, key):
        key = int(key)
        if self.multiset.get(key):
            self.multiset[key] -= 1

    def result(self) -> int:
        multiset_list = []
        for key in self.multiset:
            if self.multiset[key] > 0:
                for i in range(self.multiset[key]):
                    multiset_list.append(key)
        '''
        for key in filter(lambda x: self.multiset[x] > 0, self.multiset):
            for _ in range(self.multiset[key]):
                multiset_list.append(key)
        '''

        result = reduce(lambda x, y: x ^ y, multiset_list)
        return result

    def _plus_one(self, _arg):
        self.multiset = {key + 1: self.multiset[key] for key in self.multiset}

    def _add_key(self, new_key):
        new_key = int(new_key)
        if self.multiset.get(new_key):
            self.multiset[new_key] += 1
        else:
            self.multiset[new_key] = 1

    def _minus_one(self, key):
        key = int(key)
        if self.multiset.get(key):
            self.multiset[key] -= 1

    def execute(self, request: list):
        mapping = {
            '1': self._plus_one,
            '2': self._add_key,
            '3': self._minus_one
        }
        type_ = request[0]
        key = request[1] if len(request) > 1 else None

        mapping[type_](key)


# n, q = map(int, input().split())
# string = input()
# multiset = Multiset(string)
# print(multiset.multiset)
# result_xor = []
# for _ in range(q):
#     request = input().split()
#     type_i = int(request[0])
#     if type_i == 1:
#         multiset.plus_one(1)
#     elif type_i == 2:
#         multiset.add_key(int(request[1]))
#     else:
#         multiset.minus_one(int(request[1]))
#     result_xor.append(multiset.result())
# print(*result_xor, sep="\n")

n, q = map(int, input().split())
string = input()
multiset = Multiset(string)
print(multiset.multiset)
result_xor = []
for _ in range(q):
    request = input().split()

    multiset.execute(request)

    result_xor.append(multiset.result())
print(*result_xor, sep="\n")
