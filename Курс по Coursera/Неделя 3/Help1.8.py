n = int(input())
m = []
while n != 0:
    m.append(n)
    n = int(input())
n1 = len(m)
s = sum(m) / n1
k = 0
sum1 = 0
while n1 > k:
    sum1 += (m[k] - s) ** 2
    k += 1
n2 = (sum1 / (n1 - 1)) ** 0.5
print(n2)
