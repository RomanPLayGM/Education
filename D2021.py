n = int(input())
m = []
L = n
m1 = []
r = 0
st = "".join(map(str, input().split()))
for j in st:
    m.append(int(j))
m1.append(sum(m))
print(m[-1])
for i in range(L):
    while -i != -(m[0]):
        m1.append(sum(m[-i], [m[-i-1]]))
