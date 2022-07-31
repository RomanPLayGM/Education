n = list(input())
h = []
h1 = []
k = 0
k1 = -1
for i in n:
    if i != " ":
        h.append(n[k])
        h1.append(n[k1])
        k += 1
        k1 += -1
    else:
        break
for i in h1:
    if i == " ":
        del h1[-1]
h2 = "".join(h)
h3 = "".join(h1)
if len(h3) <= len(h2):
    n.reverse()
k = 0
k1 = -1
h4 = []
h5 = []
for j in n:
    if j != " ":
        h4.append(n[k])
        h5.append(n[k1])
        k += 1
        k1 += -1
    else:
        break
#else:
    #h1.reverse()

if len(h3) < len(h2):
    h1.reverse()
    h2 = "".join(h)
    h3 = "".join(h1)
    m = int(h2)
    m1 = int(h3)
    print((m + 1) * m1)
else:
    h4.reverse()
    h2 = "".join(h4)
    h3 = "".join(h5)
    m = int(h3)
    m1 = int(h2)
    print((m + 1) * m1)