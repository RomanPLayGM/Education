
#h1 = [i.lower() for i in a]
h2 = list(input().replace(' ', '').lower())
h3 = sorted(set(h2))
h4 = str
for j in h3:
    if j == h2[h2.index(j)]:
        del h2[h2.index(j)]
h4 = "".join(h2)
print(h4)
print("".join(h3))