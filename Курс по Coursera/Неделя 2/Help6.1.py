a = [1, 1] + [1, 2]
a = {1: "one", 2:"two"}
b = [1, 2, 6, 7]
print(list(map(lambda x: a.get(x, x), b)))