with open('input.txt', 'r', encoding='utf8') as fin:
    k, s = int(fin.readline()), []
    for i in fin:
        score = list(map(int, i.split()[-3:]))
        if min(score) > 39:
            s.append(sum(score))
with open('output.txt', 'w', encoding='utf8') as fot:
    if len(s) <= k or k == 0:
        print(0, file=fot)
    else:
        s.sort(reverse=True)
        a = 1
        for j in s[:k+1]:
            if j > s[k]:
                a = j
        print(a, file=fot)
