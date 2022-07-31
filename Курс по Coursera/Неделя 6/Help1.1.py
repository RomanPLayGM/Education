k = int(input())
m1 = list(map(int, input().split()))
if k == len(m1) and len(m1) <= 10**9:
    m1.sort()
print(*m1)
