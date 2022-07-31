s = input()
k = 0
s1 = ""
while len(s) > k:
    s1 += s[k] + "*"
    k += 1
print(s1[:-1])
