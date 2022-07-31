s = input()
pos = s.find("h")
s1 = s[pos + 1:]
s2 = s1[::-1]
pos1 = s2.find("h")
pos2 = len(s) - pos1 - 1
news = (s[:pos] + s[pos:pos2] + s[pos + 1:pos2] + s[pos2:])
print(news)
