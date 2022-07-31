s = input()
pos = s.find("f")
s1 = s[pos + 1:]
s2 = s[:pos + 1]
pos1 = s1.find("f")
pos2 = s1.find("f") + len(s2)
if pos != -1 and pos1 == -1:
    print(-1)
if pos == -1 and pos1 == -1:
    print(-2)
if pos != -1 and pos1 != -1:
    print(pos2)
