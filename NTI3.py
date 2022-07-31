from collections import deque
n = int(input())
s = input()
m = deque('0')
k = 1
m1 = []
for i in s:
    if i == "R":
        m.append(k)
        k += 1
    else:
        m.appendleft(k)
        k += 1
for j in m:
    m1.append(str(j))
print(" ".join(m1))