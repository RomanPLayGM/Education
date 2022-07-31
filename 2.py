# def helper(n1, m1, array1):
#     if n1 < 1 or m1 < 1:
#         return 0
#     if n1 == 1 and m1 == 1:
#         return 1
#     if array1[n1][m1] != 0:
#         return array1[n1][m1]
#     array1[n1][m1] = helper(n1 - 1, m1, array1) + helper(n1, m1 - 1, array1)
#     return array1[n1][m1]
#
#
# def paths(n, m):
#     return helper(n, m, [[0 for i in range(m + 1)] for x in range(n + 1)])
#
# def uniquePaths1(m: int, n: int) -> int:
#   memo = [[0 for j in range(n)] for i in range(m)]
#   for i in range(m):
#       memo[i][0] = 1
#   for j in range(n):
#       memo[0][j] = 1
#   for i in range(1, m):
#       for j in range(1, n):
#           memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
#   return memo[-1][-1]
# N, M = map(int, input().split())
# print(paths(N, M))


def uniquePaths(m, n):
    memo = [[1 for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]


N, M = map(int, input().split())
print(uniquePaths(N, M))

