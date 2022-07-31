T = int(input())
a = []
u = []
for i in range(T):
    k, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    y = 0
    t = 0
    for n in a:
        if y <= m:
            y += n
            t += 1
    t -= 1
    u.append(t)
for i in range(T):
    print("Case #", i+1, ":", u[i])
