words = {}
with open('input.txt') as in_file:
    for w in in_file.read().split():
        words[w] = words[w] + 1 if w in words else 0
print(sorted(words, key=lambda x: (-words[x], x))[0])
