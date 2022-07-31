words = {}
in_file = open('input.txt')
for w in in_file.read().split():
    words[w] = words[w] + 1 if w in words else 1
print(*sorted(words, key=lambda x: (-words[x], x)), sep='\n')
