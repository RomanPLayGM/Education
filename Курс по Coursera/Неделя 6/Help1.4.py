fin = open('input.txt', 'r', encoding='utf-8')
lin = fin.readlines()
a = []
for now in lin:
    b = list(now.split())
    c = b[0], b[1], b[3]
    a.append(c)
a.sort()
for name in a:
    print(*name)
