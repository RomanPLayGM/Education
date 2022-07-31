n = float(input())
v = (n * 1000) / 3600
s1 = 1000 / v
m = int(s1 // 60)
s = round(s1 % 60)
if s == 60:
	s = 0
	m += 1
	print(m, s)
else:
	print(m, s)