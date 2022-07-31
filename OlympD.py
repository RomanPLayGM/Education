m = ['-1', '2', '0']
st1 = []
for u in m:
    st1.append(int(u))
n = 3
b = min(st1)
for t in range(n):
    for j in st1:
        o = st1.index(j)
        j -= b
        if j == 0:
            st1.remove(j)
            b = min(st1)
        else:
            st1[o] = j
print(st1)