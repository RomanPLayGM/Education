d, s, h = {}, 0, 450
with open('input.txt') as in_file:
    for line in in_file:
        d[' '.join(line.split()[:-1])] = int(line.split()[-1])
        s += int(line.split()[-1])
d = [[m, int(h * d[m] / s), h * d[m] / s - int(h * d[m] / s)] for m in d]
overall = sum(party[1] for party in d)
for party in sorted(d, key=lambda x: (-x[2], -x[1])):
    if overall == h:
        break
    party[1], overall = party[1] + 1, overall + 1
print(*[' '.join(map(str, party[:2])) for party in d], sep='\n')
