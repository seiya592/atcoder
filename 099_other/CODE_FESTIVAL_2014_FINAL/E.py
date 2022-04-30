def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

# 解説AC

N = II()
R = LIIS()
dp = [[0]*2 for _ in range(N)]
#dp[n番目まで][0:最後にレートが下降した / 1:レートが上昇した] = 個数
dp[0][0] = 1
dp[0][1] = 1
for n in range(1,N):
    for k in range(n):
        if R[n] < R[k]:
            dp[n][0] = max(dp[k][1] + 1, dp[n][0])
        if R[n] > R[k]:
            dp[n][1] = max(dp[k][0]+1, dp[n][1])
print(0 if max(dp[N-1])< 3 else max(dp[N-1]))


# N = II()
# R = LIIS()
#
# dp = [[[10**10,-10**10] for _ in range(N+1)] for _ in range(N)]
# # for n in range(N):
# #     for c in range(N+1):
# #         dp[n][c][0] = 10**10
# #         dp[n][c][1] = -10**10
# dp[0][0][0] = R[0]
# dp[0][0][1] = R[0]
#
# #dp[n番目の数まで][ならずもの数の個数][0:最後にレートが下降した / 1:レートが上昇した] = 最後のレーティングの値
# for n in range(N-1):
#     for c in range(0,n+1):
#         # nを選ばない場合
#         dp[n+1][c][0] = min(dp[n][c][0],dp[n+1][c][0])
#         dp[n + 1][c][1] = max(dp[n][c][1], dp[n + 1][c][1])
#
#         #nを選べる場合
#         if R[n+1] < dp[n][c][1]:
#             dp[n+1][c+1][0] = min(R[n+1], dp[n+1][c+1][0])
#
#         if R[n+1] > dp[n][c][0]:
#             dp[n + 1][c + 1][1] = max(R[n+1], dp[n + 1][c + 1][1])
#
# ans = 0
# for n in range(N+1):
#     if dp[N-1][n][0] != 10**10 or dp[N-1][n][1] != -10 ** 10:
#        ans = n+1
# print(0 if ans < 3 else ans)