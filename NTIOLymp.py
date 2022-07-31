
a = input()
y1 = list(a)
#h1 = [i.lower() for i in a]
h1 = "".join([x.replace(' ', '') for x in y1])
h7 = "".join([i.lower() for i in h1])
h2 = list(h7)
h3 = sorted(list(set(h2)))
h4 = str
for j in h3:
    if j == h2[h2.index(j)]:
        del h2[h2.index(j)]
h4 = "".join(h2)
print(h4)
print("".join(h3))
#e wew e w
#len(h2) != len(h3) мб в 19 строчку кода
