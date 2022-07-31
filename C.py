n = int(input())
a = input().split()
m = []
for i in a:
    m.append(int(i))
t = sum(m)
t1 = bin(t)
newt = t1[2:]
print(len(newt))
n = int(input())
numbers = [int(i) for i in input().split()]
print(n + sum(numbers))
print(n + sum(numbers) // (2 ** n))

