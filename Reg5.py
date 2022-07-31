t = int(input())
all_answers = []
for i in range(t):
    n, a, b = map(int, input().split())
    max_a_b = max(a, b) // n
    min_a_b = min(a, b) // n
    t1 = (min(a, b) // n) * (max_a_b + 1)
    t2 = (min(a, b) - (min(a, b) // n) + 1) * max_a_b
    t3 = t1 + t2
    all_answers.append(t3)
    # total = (a + 1) * (b + 1) - 1
    # count = 0
    # for a_i in range(0, a + 1):
    # new_b = (n + (abs(a_i - 1) // n) * n) - a_i
    # count += len(range(new_b, b + 1, n))
    # all_answers.append(count)
print(*all_answers, sep='\n')
# max_a_b = max(a, b) // n
# min_a_b = min(a, b) // n
# t1 = (min(a, b) // n) * (max_a_b + 1)
# t2 = (min(a, b) - (min(a, b) // n) + 1) * max_a_b
# print(max_a_b)
# print(min_a_b)
print(t1)
print(t2)
