


def steck_d(string):
    steck = []
    dict_sc = {")": "(", "]": "[", "}": "{"}
    for i in string:
        if i not in dict_sc:
            steck.append(i)
        else:
            if len(steck) == 0 or dict_sc[i] != steck[-1]:
                return False
            else:
                steck.pop()
    return not steck


def check(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        print(stack, f": {i}")
        if i in brackets_open:
            print("Opened")
            stack.append(i)
        if i in brackets_closed:
            print("Closed")
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            print(index)
            open_bracket = brackets_open[index]
            print(open_bracket)
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return False
    return not stack


def check_steck(s):
    lookup = {")": "(",
              "}": "{",
              "]": "["}

    stack = []

    for i in range(len(s)):
        if s[i] not in lookup:
            stack.append(s[i])

        else:
            if len(stack) == 0 or stack[-1] != lookup[s[i]]:
                return False
            stack.pop()

    return len(stack) == 0


string_el = list(map(str, input()))
print(steck_d(string_el))
print(check(string_el))
print(check_steck(string_el))


def run_sum(list_):
    list_0 = [list_[0]]
    for i in range(1, len(list_)):
        r = list_0[i - 1] + list_[i]
        list_0.append(r)
    return list_0


# s = 0
# return [s := s + v for _, v in enumerate(list_)] - Крутое решение
list_sum = list(map(int, input().split()))
print(run_sum(list_sum))


def add(len_1, len_2):
    len_reversed_1 = int("".join(reversed(len_1)))
    len_reversed_2 = int("".join(reversed(len_2)))
    sum_reversed = str(len_reversed_1 + len_reversed_2)
    reversed_sum = list(reversed(sum_reversed))
    array_s = []
    for i in reversed_sum:
        array_s.append(int(i))
    return array_s
# def y(l1, l2):
#     n1 = ""
#     n2 = ""
#
#     itr1 = l1
#     itr2 = l2
#     while itr1 or itr2:
#         if itr1:
#             n1 += str(itr1.val)
#             itr1 = itr1.next
#         if itr2:
#             n2 += str(itr2.val)
#             itr2 = itr2.next
#     n1 = n1[::-1]
#     n2 = n2[::-1]
#     n3 = str(int(n1) + int(n2))[::-1]
#     l3 = ListNode(n3[0])
#     itr = l3
#     for i in range(1, len(n3)):
#         itr.next = ListNode(int(n3[i]))
#         itr = itr.next
#     return l3
#
# l1 = list(map(str, input().split()))
# l2 = list(map(str, input().split()))
# print(add(l1, l2))


def permutations(string):
    result = {string}
    # print(result, 1, 1)
    if len(string) == 2:
        result.add(string[1] + string[0])
        # print(result, 0, 2)
    elif len(string) > 2:
        # print(result, 1, 2)
        for i, c in enumerate(string):
            # print("i:", i, "|||||", "c:", c)
            # print(string[:i], "- :i")
            # print(string[i + 1:], "- i + 1")
            # print("string[:i] + string[i + 1:] -----", string[:i] + string[i + 1:])
            for s in permutations(string[:i] + string[i + 1:]):
                # print("s:", s, "|", "c:", c)
                # print(result, 3)
                # print("c + s -----", c + s)
                result.add(c + s)
                # print(result, ": add")
    # print(result, 1, 3)
    # print(len(list(result)))
    return list(set(result))

# def permutations(string):
#   if len(string) == 1: return set(string)
#   first = string[0]
#   rest = permutations(string[1:])
#   result = set()
#   for i in range(0, len(string)):
#     for p in rest:
#       result.add(p[0:i] + first + p[i:])
#   return result
# def permutations(s):
#     if len(s) == 0:
#         return []
#     elif len(s) == 1:
#         return [s]
#     else:
#         return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))
# def permutations(s):
#     if(len(s)==1): return [s]
#     result=[]
#     for i,v in enumerate(s):
#         result += [v+p for p in permutations(s[:i]+s[i+1:])]
#     return list(set(result))


n = input()
print(permutations(n))


# def count(n):
#     if n < 10:
#         return n
#     tmp = n
#     rank = 1
#     len_n = 1
#     while tmp > 9:
#         tmp /= 10
#         rank *= 10
#         len_n += 1
#     return len_n * (n + 1 - rank) + count(rank - 1)
#
#
# n_1 = int(input())
# print(count(n_1))
