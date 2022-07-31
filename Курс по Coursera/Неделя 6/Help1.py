def merge(a, b):
    c = a + b
    for i in range(len(c) - 1):
        for j in range(i, len(c)):
            if c[j] <= c[i]:
                c[j], c[i] = c[i], c[j]
    print(*c)


a1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))
merge(a1, b2)
