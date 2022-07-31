s_s = set(str(i) for i in range(1, int(input())+1))
while True:
    print(s_s)
    line = set(input().split())
    if line == {"HELP"}:
        break
    line_s = input().split()
    if line_s == ["YES"]:
        s_s &= line
    elif line_s == ["NO"]:
        s_s -= line
print(*sorted(list(s_s), key=int))
