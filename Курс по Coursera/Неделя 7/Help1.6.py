with open("input.txt") as fin:
    w_l = fin.read().split()
words = {}
for w in w_l:
    words[w] = words[w] + 1 if w in words else 0
    print(words[w], end=" ")
