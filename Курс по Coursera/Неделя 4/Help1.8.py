def xor(x, y):
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        return True
    else:
        return False


x1, y1 = float(input()), float(input())
if xor(x1, y1):
    print(1)
else:
    print(0)
