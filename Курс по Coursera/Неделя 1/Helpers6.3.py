a = int(input())
b = int(input())
print(a % b)
c1 = 0 ** (a % b)
print(c1)
c2 = 0 ** c1
print(c2)
print("YES"*(0**c2), "NO"*(0 ** c1), sep="")
# h = 0**c1
# h1 = h - 1
# print("YES"*(0 ** h), "NO"*(h + h1), sep="")
