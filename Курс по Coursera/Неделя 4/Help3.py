def sums(n, cur_sum=0, a=None):
    a = a or []
    if len(a) > 4:
        return
    if cur_sum == n:
        return a
    for i in range(int((n - cur_sum) ** 0.5), 0, -1):
        res = sums(n, cur_sum + i ** 2, a + [i])
        if res:
            return res


print(sums(int(input())))
