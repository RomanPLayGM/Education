intList = list(map(int, input().split()))
n = intList[0]
for i in intList:
    if i > n:
        print(i, end=' ')
        n = i
    else:
        n = i
