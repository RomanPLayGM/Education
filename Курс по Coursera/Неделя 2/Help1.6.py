a = int(input())
b = int(input())
if a == b:
    print("YES")
    exit()
if (a - 1) % (b - a + 1) == 0:
    print("YES")
else:
    print("NO")
