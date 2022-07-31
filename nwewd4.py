from numba import njit
A = int(input())
B = int(input())
K = int(input())
@njit(fastmath=True)
def RTR(a, b, k):
    while k > 0:
        while a >= b and k > 0:
            a -= 1
            k -= 1
        while b >= A and k > 0:
            b -= 1
            k -= 1
        k -= 1
    print(a, b)
RTR(A, B, K)