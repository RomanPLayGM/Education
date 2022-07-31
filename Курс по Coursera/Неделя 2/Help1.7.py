a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
a2 = a % 2
a3 = a1 % 2
b2 = b % 2
b3 = b1 % 2
if b2 == b3:
    if a2 == a3:
        print("YES")
    else:
        print("NO")
else:
    if a2 == a3:
        print("NO")
    else:
        print("YES")
# if a == a1:
    # if b1 > b:
        # if (b1 - b) % 2 == 0:
            # print("YES")
        # else:
            # print("NO")
    # else:
        # if (b - b1) % 2 == 0:
            # print("YES")
        # else:
            # print("NO")
# elif b == b1:
    # if a1 > a:
        # if (a1 - a) % 2 == 0:
            # print("YES")
        # else:
            # print("NO")
    # else:
        # if (a - a1) % 2 == 0:
            # print("YES")
        # else:
            # print("NO")
# else:
