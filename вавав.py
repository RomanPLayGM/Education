b = int(input())
y = []
k = 1
for i in range(b):
    t = int(input())
    if t % 10 == 4:
        y.append(t)
min1 = y[0]
while k < len(y):
    if y[k] < min1:
        min1 = y[k]
    k += 1
print(min1)