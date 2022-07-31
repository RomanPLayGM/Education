n = int(input())
a = list(map(int, input().split()))
x = int(input())
m = a[0]
r = abs(x - m)
for i in a:
    if abs(i - x) < r:
        m = i
        r = abs(x - m)
print(m)
