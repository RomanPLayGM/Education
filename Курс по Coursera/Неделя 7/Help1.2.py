list_0 = list(map(int, input().split()))
b = set()
for i in list_0:
    print('YES' if i in b else 'NO')
    b.add(i)
