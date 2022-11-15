"""
2022/09/24 20:51:03
"""
import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N, K = IIS()
A = LIIS()

dp = [0] * (N+1)
# dp[山の残数がnの時点での] = その時の手番の人が取れる最大の石の数

# 貰うDP
for n in range(1, N+1):
    for a in A:
        if a > n:   # 要素外避け
            continue
        # dp[n] = max(dp[n], a+(n-a)-dp[n-a])
        tmp = (n-a) - dp[n-a]       # 山の数が n個 の時のプレイヤーが過去入手していた石 = 1手番前の「2人」が取れる石の数 - 1手番前のプレイヤーの石の数
        dp[n] = max(dp[n], tmp + a)     # 過去入手していた石の最大数 + 今回入手する予定の石

print(dp[N])


# N,K = IIS()
# A = LIIS()
#
# dp = [[]]

#
# N,K = IIS()
# A = LIIS()
# B = []
# for a in reversed(A):
#     B.append(-a)
#
# ans = 0
# flg = 1
# while N:
#     i = bisect.bisect_left(B,-N)
#     if flg:
#         ans += B[i]
#     N += B[i]
#     flg ^= 1
# print(abs(ans))

# dp = [-INF] * (N+1)
# dp[0] = 1
#
# for n in range(N):
#     for k in A:
#         if n+k <= N:
#             dp[n+k] += dp[n]
#
# center = ((N+1) // 2)
# ans = 0
# for i in range(1,N):
#     if dp[i+center] and dp[i-center]:
#         print(center+i)
#         exit()


# N,K = IIS()
# A = LIIS()
#
# dp = [[0]*2 for _ in range(N+1)]
# #dp[n個の山を作る際に][1=takahashi] = 最大数
#
# for n in range(1,N):
#     for i in range(2):
#         for k in A:
#             if n-k > 0:
#                 continue
#             if i == 0:
#                 a = -k
#             else:
#                 a = k
#             dp[n][i] = max(dp[n-k][i^1] + a, dp[n][i])
# pass
# dp = [[-INF,-INF] for _ in range(N+1)]
# #dp[山の残りがN個][1=高橋のターン] = 高橋の得点
# dp[N][0] = 0
# # dp[N][1] = 0
# for n in range(N,0,-1):
#     for t in range(2):
#         if t:
#             for k in A:
#                 if n-k >= 0:
#                     dp[n-k][t] = max(dp[n-k][t],dp[n][t^1] + k)
#         else:
#             for k in A:
#                 if n - k >= 0:
#                     dp[n - k][t] = max(dp[n - k][t], dp[n][t^1] + k)
# print(dp[0])