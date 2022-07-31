t = int(input())
array = []
for y in range(t):
    len_permutation = int(input())
    permutation = list(map(int, input().split()))
    tree = {}
    cash = set()
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if permutation[i] > permutation[j]:
                cash.add(permutation[j])
        if len(cash) == 0:
            cash = {0}
        tree[permutation[i]] = cash
        cash = set()
    print(tree)
    cash = tree[permutation[0]]
    print(cash)
    for i in permutation:
        if i == permutation[0]:
            continue
        else:
            if tree[i] == {0}:
                if len({i} & cash) != 0:
                    cash.add(i)
                    del tree[i]
            else:
                if len(tree[i] & cash) != 0:
                    cash = set(list(cash) + list(tree[i]))
                    cash.add(i)
                    del tree[i]
                else:
                    if tree[i] != {0}:
                        for j in tree[i]:
                            cash.add(j)
                    else:
                        if len({i} & cash) != 0:
                            cash.add(i)
                            del tree[i]
    array.append(len(tree))
print(*array, sep="\n")

