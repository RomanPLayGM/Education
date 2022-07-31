a = int(input())
b = int(input())
k = ""
for i in range(a, b + 1):
    k = int("".join(reversed(str(i))))
    if i == k:
        print(i)
