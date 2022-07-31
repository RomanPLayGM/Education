s = input()
pos = s.find("f")
s1 = s[pos + 1:]
s2 = s1[::-1]
pos1 = s2.find("f")
if pos != -1:
    print(pos, end=" ")
if pos1 != -1:
    pos1 = len(s) - pos1 - 1
    print(pos1)
