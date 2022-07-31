def count_sort(lst):
    c, result = [0] * 101, ''
    for now in lst:
        c[now] += 1
    for i in range(101):
        result += (str(i) + ' ') * c[i]
    return result


my_list = list(map(int, input().split()))
print(count_sort(my_list))
