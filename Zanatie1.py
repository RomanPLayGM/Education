for A in range(1, 1000):
    good = True
    for x in range(1, 10000):
        f = (110 % A == 0) and (((x % 80 == 0) and (x % 75 == 0)) <= (x % A == 0))
        if f == 0:
            good = False
            break
    if good == True:
        print(A)



