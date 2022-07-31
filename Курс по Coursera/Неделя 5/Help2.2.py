def IsAscending(A):
    k = 0
    p = True
    for i in range(1, len(A)):
        if A[i] > A[k]:
            k = i
            continue
        else:
            p = False
            break
    return print("YES" * 0 ** (not p), "NO" * 0 ** p, sep="")


a = list(map(int, input().split()))
IsAscending(a)
