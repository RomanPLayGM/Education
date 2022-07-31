x, y = int(input()), int(input())
x1, y1 = int(input()), int(input())
if y1 > y:
    if y % 2 == 0:
        if x % 2 == 0:
            if y1 % 2 == 0:
                if x1 % 2 == 0:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                if x1 % 2 == 0:
                    print("NO")
                else:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
        else:
            if y1 % 2 == 0:
                if x1 % 2 == 0:
                    print("NO")
                else:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
            else:
                if x1 % 2 == 0:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
    else:
        if x % 2 == 0:
            if y1 % 2 == 0:
                if x1 % 2 == 0:
                    print("NO")
                else:
                    if x1 - y1 <= 1:
                        print("YES")
                    else:
                        print("NO")
            else:
                if x1 % 2 == 0:
                    if x1 - y1 <= 1:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
        else:
            if y1 % 2 == 0:
                if x1 % 2 == 0:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                if x1 % 2 == 0:
                    print("NO")
                else:
                    if x1 <= y1:
                        print("YES")
                    else:
                        print("NO")
else:
    print("NO")
