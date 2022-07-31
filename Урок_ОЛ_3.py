n = tuple(map(str, input()))
save_n = list(n)
reversed_n = tuple(reversed(n))
save_reversed_n = list(reversed_n)
array_n = set()
array_reversed_n = set()
permutations_set = set()
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            continue
        save_n[i], save_n[j] = save_n[j], save_n[i]
        save_reversed_n[i], save_reversed_n[j] = save_reversed_n[j], save_reversed_n[i]
        array_n.add("".join(save_n))
        array_reversed_n.add("".join(save_reversed_n))
        save_n = list(n)
        save_reversed_n = list(reversed_n)
# print(array_n)
# print(array_reversed_n)
permutations_set.add("".join(n))
for i in array_n & array_reversed_n:
    if i == set():
        continue
    permutations_set.add(i)
for i in array_n | array_reversed_n:
    if i == set():
        continue
    permutations_set.add(i)
permutations_set.add("".join(reversed_n))
print(list(permutations_set))
print(len(permutations_set))
