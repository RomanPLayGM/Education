fin = open('input.txt')
f = fin.read().split()
dictionary = dict()
for i in range(len(f) // 2):
    dictionary[f[2 * i]] = dictionary.get(f[2 * i], 0) + int(f[2 * i + 1])
for name, count in sorted(dictionary.items()):
    print(name, count)
