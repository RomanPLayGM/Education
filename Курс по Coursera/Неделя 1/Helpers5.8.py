n = int(input())
n = n % (24 * 60 * 60)
# print(n)
h = n // (60 * 60)
n = n % (60 * 60)
# print(n)
m = str(n // 60)
# print(m)
# print(int(m) // 10)
# print(0**(int(m) // 10)*"0")
s = str(n % 60)
# print(s)
# print(int(s) // 10)
print(h, ":", 0**(int(m) // 10)*"0"+m, ":", 0**(int(s) // 10)*"0"+s, sep="")
