n, m = map(int, input().split())
glass = ""
while n * m > len(glass):
    s = input()
    glass += s
y = glass[m:n * m - m]
u1 = glass[:m]
u2 = glass[n * m - m:]
# print(u2)
# print(y)
# print("------")
# print(glass[n*m - m:])
k = input()
m1 = []
k1 = 0
for i in range(int(k)):
    name, count, symbol = map(str, input().split())
    y1 = list(reversed(y))
    y2 = y1[k1:m * int(count) + k1]
    k1 = m * int(count)
    for j in y2:
        if j == " ":
            j = symbol
            m1.append(j)
        else:
            m1.append(j)
m1.reverse()
m2 = u1 + "".join(m1) + u2
k2 = 0
for i in m2:
    k2 += 1
    if k2 == m:
        print(i)
        k2 = 0
    else:
        print(i, end="")
