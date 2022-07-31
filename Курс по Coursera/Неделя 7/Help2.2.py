n = int(input())
set_n = set(range(1, n + 1))
string = []
while True:
    line_s = set(input().split())
    if line_s == {"HELP"}:
        break
    line_s_1 = set()
    for i in line_s:
        line_s_1.add(int(i))
    line = set_n & line_s_1
    if len(line) > len(set_n) // 2:
        string.append("YES")
        set_n -= set_n - line
    else:
        string.append("NO")
        set_n -= line
for i in string:
    print(i)
print(*sorted(list(set_n)))
