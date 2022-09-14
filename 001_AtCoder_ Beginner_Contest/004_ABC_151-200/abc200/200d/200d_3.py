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
import sys
sys.setrecursionlimit(500000)
INF = 10**10

"""
解けてない
"""

# N = II()
# A = LIIS()
#
# #dp[n個目までの数で][i%200の値を作れる] = 組み合わせ数
# dp = [[0]*200 for _ in range(N+1)]
# dp[0][0] = 1
#
# for n in range(N):
#     for i in range(200):
#         dp[n+1][i] += dp[n][i]
#         dp[n+1][(i+A[n])%200] += dp[n][i]
#
# num = -1
# for i, d in enumerate(dp[-1]):
#     if d >= 2:
#         num = i
#
# if num == -1:
#     NO()
#
# # 復元する
# def calc(num):
#     ret = []
#     now = num
#     for n in reversed(range(N)):
#         tmp = (now + 200 - (A[n]%200))%200
#         if dp[n][tmp]:
#             dp[n+1][now] -= dp[n][tmp]
#             ret.append(n+1)
#             now = tmp
#         else:
#             # A[n]を選んでない
#             dp[n+1][now] -= dp[n][now]
#
#     return ret
# B = []
# c = []
#
# B = calc(num)
# C = calc(num)
# while B == C:
#     C = calc(num)
# print('Yes')
# print(len(B), *sorted(B))
# print(len(C), *sorted(C))