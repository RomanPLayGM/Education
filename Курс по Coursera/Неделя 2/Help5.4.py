n = int(input())
count = 1
count1 = 1
m = 1
while n != 0:
    k = n
    n = int(input())
    if n > k and n != 0:
        count += 1
        count1 = 1
        if count >= m:
            m = count
    elif n < k and n != 0:
        count1 += 1
        count = 1
        if count1 >= m:
            m = count1
    elif n == k and n != 0:
        count = count1 = 1
print(m)
