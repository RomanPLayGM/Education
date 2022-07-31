l = int(input())
d = int(input())
k = int(input())
c = 0
while k > 1 and l > d:
    c += 1
    l -= d
    k -= 1
    if l == d:
        c += 1
print(c)
L = int(input())
D = int(input())
K = int(input())
if L == D * K:
    print(K)
else:
    print(min(K - 1, L // D))