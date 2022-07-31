class Person(object):
    pass


a = Person()
c = Person()
print(hash(a), hash(c))
print(id(a), id(c))
print(a == c)
a = (1, 2, 3)
print(hash(a), 2)
print(id(a), 2)
t = a
# print(hash(a))
# print(id(a))


def f(*args, **kwargs):
    print(type(args))
    for i in args:
        print(i)
    for i in kwargs:
        print(i)


f(1, 2, d=6, q={1, 2, 3})


def f1(y2):
    y2 = 3
    print(id(y2))


def second(y1):
    y1.append(4)
    a = y1.copy()
    print(id(a))
    print(y1, id(y1))


x = [1, 2, 3]
print(id(x))
f1(x)
second(x)


def out(y):
    print(x)


    def i(t):
        print(x)


    i(1)

x = 2
out(x)
#  декораторы, замыкание
def counter(n, a, b):
    count = 0
    for a_i in range(0, a + 1):
        new_b = (n + (abs(a_i - 1) // n) * n) - a_i
        count += len(range(new_b, b + 1, n))
        print(a_i, count)
    return count


t = int(input())
all_answers = []
for i in range(t):
    n, a, b = map(int, input().split())
    # min_a_b = min(a, b) // n
    # max_a_b = max(a, b) // n
    # total = min(a, b) - min_a_b + 1
    # max_a_b_1 = max_a_b + 1
    # count = min_a_b * max_a_b_1 + total * max_a_b
    if a < b:
        all_answers.append(counter(n, a, b))
    else:
        all_answers.append(counter(n, b, a))
    # all_answers.append(count)
print(*all_answers, sep='\n')