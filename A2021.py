n = int(input())
v = int(input())
kbd = int(input()) # количество задач в будний день
kvd = int(input()) # количество задач в выходной день
d = []
k = 1
s = 0
for i in range(1, n + 1):
    d.append(i)
for j in d:
    if j == v:
        v *= k
        k += 1
        s += kvd
    else:
        s += kbd
print(s)