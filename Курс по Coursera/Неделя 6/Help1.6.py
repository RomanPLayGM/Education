k = int(input())
m = []
for i in range(k):
    name, number = list(map(str, input().split()))
    m.append([name, number])
    m[i][1] = int(m[i][1])
    m[i][0], m[i][1] = m[i][1], m[i][0]
m.sort(reverse=True)
for i in range(k):
    print(m[i][1])
