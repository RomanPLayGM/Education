sum1, n = map(int, input().split())
k = 0
sum_0 = 0
m1 = []
for i in range(n):
    m1.append(int(input()))
m1.sort()
for i in m1:
    sum_0 += i
    if sum_0 <= sum1:
        k += 1
print(k)
