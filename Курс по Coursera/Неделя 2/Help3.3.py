x = int(input())
y = int(input())
x1 = 0
k = 1
while y > x:
    x1 = x * 0.1
    x += x1
    k += 1
print(k)
