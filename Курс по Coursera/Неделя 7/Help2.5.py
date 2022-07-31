number_vas = input()
kod = '495'
N = number_vas.replace('-', '')
N = N.replace('(', '')
N = N.replace(')', '')
N = N.replace(' ', '')
if len(N) == 7:
    N = kod + N
else:
    N = N[-10:]
numbers = (input(), input(), input())
new_numbers = []
for i in numbers:
    x = i.replace('-', '')
    x = x.replace('(', '')
    x = x.replace(')', '')
    x = x.replace(' ', '')
    if len(x) == 7:
        x = kod + x
    else:
        x = x[-10:]
    new_numbers.append(x)
for j in new_numbers:
    if j == N:
        print('YES')
    else:
        print('NO')
