n = int(input())
k = 1
u = 0
if n == 1:
    print("YES")
    exit()
while n >= k:
    k *= 2
    if n == k:
        u += True
    else:
        u += False
if u == 1:
    print("YES")
else:
    print("NO")
