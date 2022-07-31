import math
n, a, b = map(int, input().split())
string_b_s = input()
number_off_actions = math.floor(math.log2(n))
new_n = int((2 ** number_off_actions) / 2) - 1
for j in range(number_off_actions):
    print(string_b_s)
    mid = math.floor(len(string_b_s) / 2)
    print(mid + 1)
    string_b_s = string_b_s[:mid]
    print(string_b_s, "!")
for i in range(new_n):
    for j in range(2):
        print(j)
