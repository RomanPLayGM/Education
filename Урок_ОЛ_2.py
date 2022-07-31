n = int(input())
sum_0 = 0
for i in range(1, n + 1):
    sum_0 += len(str(i))
print(sum_0)

#

print(sum(map(lambda x: len(str(x)), range(1, n + 1))))


print("------------------")
n = int(input())
i = 1
while n - len(str(i)):
    n -= len(str(i))
    i += 1
print(i)
