n = int(input())
m_0 = list(map(int, input().split()))
m_0.sort()
count = 0
for i in m_0:
    if i >= n:
        count += 1
        n = i + 3
print(count)
