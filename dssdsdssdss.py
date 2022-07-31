def gimme(input_array):
    count = 0
    t = []
    for o in input_array:
        t.append(o)
    u = input_array
    last_item = len(u) - 1
    for z in range(0, last_item):
        for x in range(0, last_item):
            if u[x] > u[x + 1]:
                u[x], u[x + 1] = u[x + 1], u[x]
    for i in u:
        if u[0] < i < u[len(u)-1]:
            y = i
        count += 1
    l = t.index(y)
    return l
gimme([2, 3, 1])

# A = 1
# while True:
    # for x in range(0, 1000):
        # for y in range(0, 1000):
            # if not ((x * y < 4 * A) or (x >= 21) or (x < 4 * y)):
                # break
        # else:
            # continue
        # break
    # else:
        # print(A)
    # A += 1