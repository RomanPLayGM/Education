outFile = open("output.txt", "w", encoding='utf-8')
fin = open('input.txt', 'r', encoding='utf-8')
people = dict()
count = 0
for line in fin:
    people[line.strip()] = people.get(line.strip(), 0) + 1
    count += 1
p = sorted(people, key=lambda x: (-people[x], x))
if people[p[0]] > count / 2:
    print(p[0], file=outFile)
else:
    print(p[0], p[1], sep='\n', file=outFile)
outFile.close()
fin.close()
