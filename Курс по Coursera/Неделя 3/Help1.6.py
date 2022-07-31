p = float(input())
x = float(input())
y = float(input())
k = float(input())
x1 = x * 100 + y
while k != 0:
    x1 += int((x1 * p) / 100)
    k -= 1
print(int(x1 // 100), int(x1 % 100))
