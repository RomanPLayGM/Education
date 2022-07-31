a = int(input())
b = int(input())
while a > b:
    if a // 2 < b or a % 2 != 0:
        a -= 1
        print("-1")
    if a // 2 >= b:
        a //= 2
        print(":2")
