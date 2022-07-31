k = int(input())
ed = k % 10
print(ed)
dec = k // 10 % 10
print(dec)
if ed == 1 and dec != 1:
    print(k, "korova")
elif (1 < ed < 5) and dec != 1:
    print(k, "korovy")
else:
    print(k, "korov")
