a, b, c, d = map(int, input().split())
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
A, B = set(range(a, b + 1)), set(range(c, d + 1))
print(len(A & B))
