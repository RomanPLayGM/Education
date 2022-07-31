s = input()
s1 = ""
while len(s) > 0:
    s1 += s[1:3]
    s = s[3:]
print(s1)
