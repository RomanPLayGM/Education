n = int(input())
h = []
k = 0
for i in range(1, (n + 1)):
    h.append(i)
for j in h:
    if ((j + 1) - j) == 1:
        k += 1
h.reverse()
k1 = 0
k2 = 0
for j in h:
    print(len(h) - k1)
    if ((h[k1]) - h[k1+1]) == 1 and len(h) != k1:
        k2 += 1
        k1 += 1
    else:
        break
print(k2)