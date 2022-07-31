import math
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n1 = []
a = int(input())
for i in range(a):
    b = input()
    n1.append(b)
j1 = []
j2 = ''
j3 = []
for j in n1:
    for i in j:
        j1.append(i)
    j1.reverse()
    j2 = ''.join(j1)
    j3.append(j2)
    j1 = []
    j2 = ''
c = 0
n2 = []
for u in j3:
    for y in u:
        for i in range(len(n) - 1):
            if y == n[i]:
                c += math.factorial(i)*i
    n2.append(c)
    c = 0
f = 0
for j in n2:
    if j == max(n2):
        f += 1
        print(f)
    else:
        break

