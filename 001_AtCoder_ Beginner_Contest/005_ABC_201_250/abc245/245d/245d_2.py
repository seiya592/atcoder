def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# 解説AC

N, M = IIS()
A = LIIS()[::-1]
C = LIIS()[::-1]
B = [0] * (M+1)

for i in range(M+1):
    B[i] = C[i] // A[0]
    for j in range(N+1):
        C[i+j] -= A[j] * B[i]

print(*B[::-1])


# N, M = IIS()
# A = LIIS()
# C = LIIS()
# B = [0] * (M + 1)
#
# for i in range(M, -1, -1):
#     B[i] = C[N + i] // A[N]
#     for j in range(N + 1):
#         C[i + j] -= A[j] * B[i]
#
# print(*B)