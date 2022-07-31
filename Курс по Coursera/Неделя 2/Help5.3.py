n = int(input())
k = 0
s = 1
m = 1
while n != 0:
    k = n
    n = int(input())
    if k == n:
        s += 1
        if s >= m:
            m = s
    else:
        s = 1
print(m)
