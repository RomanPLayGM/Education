# Алгоритм Евклида
a = int(input())
b = int(input())
def nod(x, y): # НОД чисел
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y
def nok(x1, y1): # НОК чисел
    return (x1 * y1) // (nod(x1, y1))
print(nok(a, b))
# Сумма цифр трехзначного числа
t = list(map(int, input()))
print(sum(t))
# Бинарный поиск
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
a = list(map(int, input()))
print(a)
b = int(input("Какой элемнет: "))
print(binary_search(a, b))
# Сортировка выбором
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
    return array
a = list(map(int, input()))
print(a)
print(sel_sort(a))
# Сортировка пузырьком
def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
a = list(map(int, input()))
print(bubble(a))

