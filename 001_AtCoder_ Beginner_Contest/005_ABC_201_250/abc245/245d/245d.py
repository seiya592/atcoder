def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# N, M = IIS()
# A = LIIS()
# C = LIIS()
#
# B = [1000] * (M + 1)
# B[0] = C[0] // A[0]
#
# # for i in range(1, N + M + 1):
# #     tmp = C[i]
# #     for j, a in enumerate(A):
# #         if i >= j and  and i - j <= M:
# #             tmp -= a * B[i-j]
# #     B[i] = tmp
#
# for i in range(M+1):
