string = int(input())
string2 = int(input())
string1 = int(input())
string3 = int(input())
if string > string1:
    st = string - string1
    if string2 > string3:
        st1 = string2 - string3
        if (st == 1 or st == 0) and (st1 == 1 or st1 == 0):
            print("YES")
        else:
            print("NO")
    else:
        st2 = string3 - string2
        if (st == 1 or st == 0) and (st2 == 1 or st2 == 0):
            print("YES")
        else:
            print("NO")
else:
    st4 = string1 - string
    if string2 > string3:
        st1 = string2 - string3
        if (st4 == 1 or st4 == 0) and (st1 == 1 or st1 == 0):
            print("YES")
        else:
            print("NO")
    else:
        st2 = string3 - string2
        if (st4 == 1 or st4 == 0) and (st2 == 1 or st2 == 0):
            print("YES")
        else:
            print("NO")
