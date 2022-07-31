s = input()
pos = s.find("h")
s1 = s[::-1]
pos1 = s1.find("h")
pos2 = len(s) - pos1 - 1
s3 = s[:pos + 1]
s4 = s[pos2:]
s5 = s[pos + 1:pos2]
s6 = s5.replace("h", "H")
print(s3 + s6 + s4)
