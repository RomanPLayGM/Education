n = int(input())
x = float(input())
sum1 = 0
while n >= 0:
    n1 = float(input())
    sum1 += n1 * (x ** n)
    n -= 1
print(sum1)
