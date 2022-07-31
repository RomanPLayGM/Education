n = int(input())
s = 0
s1 = 1
s2 = n
while n > 0:
    s1 += s
    s += s1
    n -= 2
if s2 % 2 == 0:
    if s < s1:
        s = s1
else:
    if s > s1:
        s = s1
print(s)

	

def fib_help(acc1, acc, a):
	if a > 0:
		return fib_help(acc, acc + acc1, a - 1)
	else:
		return acc1

def fib(a):
	return fib_help(0, 1, a)

print(fib(50))
