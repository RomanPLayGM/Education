import statistics
m = [int(i) for i in input().split()]
n = statistics.median(m)
a1 = []
a2 = []
a3 = []
n1 = statistics.median(m)
if m[0] == n1:
    a1.append(1)
else:
    a1.append(0)
if m[1] == n1:
    a2.append(1)
else:
    a2.append(0)
if m[2] == n1:
    a3.append(1)
else:
    a3.append(0)
for i in range(0, 3):
    for j in range(0, 3):
        t = m[i]
        m[i] = m[i] - m[j]
        if m[i] == 0:
            m[i] = t
            continue
        n = statistics.median(m)
        if m[0] == n:
            a1.append(1)
        else:
            a1.append(0)
        if m[1] == n:
            a2.append(1)
        else:
            a2.append(0)
        if m[2] == n:
            a3.append(1)
        else:
            a3.append(0)
        m[i] = t
k1 = 0
k2 = 0
k3 = 0
for i in a1:
    if i == 1:
        k1 += 1
for i in a2:
    if i == 1:
        k2 += 1
for i in a3:
    if i == 1:
        k3 += 1
if k1 > 0:
    print("YES")
else:
    print("NO")
if k2 > 0:
    print("YES")
else:
    print("NO")
if k3 > 0:
    print("YES")
else:
    print("NO")
# if i == 0:
            # if m[j] == n:
                # a1.append(True)
            # else:
                # a1.append(False)
        # if i == 1:
            # if m[j] == n:
                # a2.append(True)
            # else:
                # a2.append(False)
        # if i == 2:
            # if m[j] == n:
                # a3.append(True)
            # else:
                # a3.append(False)
# u = sorted(m, key=None)
        # m2.append(u)