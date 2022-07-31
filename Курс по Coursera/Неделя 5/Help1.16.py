n = []
for i in range(10, 100):
    if i == 2 * (i % 10) * (i // 10):
        n.append(str(i))
print("".join(n))
