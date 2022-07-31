n, m = map(int, input().split())
set_an = set()
set_bo = set()
for i in range(n):
    y = int(input())
    set_an.add(y)
for i in range(m):
    y1 = int(input())
    set_bo.add(y1)
two_kit = set_an & set_bo
s_an = set_an - set_bo
s_bo = set_bo - set_an
print(len(two_kit))
print(*sorted(two_kit))
print(len(s_an))
print(*sorted(s_an))
print(len(s_bo))
print(*sorted(s_bo))
