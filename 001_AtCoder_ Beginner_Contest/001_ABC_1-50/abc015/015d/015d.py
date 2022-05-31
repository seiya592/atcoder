import copy


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20

W = II()
N,K = IIS()
AB = LLIIS(N)

# dp = [[[0]*(W+1) for _ in range(K+1)] for _ in range(N+1)]
# # dp = [n番目のスクリーンショットまでで][枚数k枚を使用したときの][幅をwまで使ったときの] = 最大の重要度
#
# #配る
# for n in range(N):
#     for k in range(K+1):
#         for w in range(W+1):
#             dp[n+1][k][w] = max(dp[n+1][k][w], dp[n][k][w]) #選ばない場合
#
#             # 選ぶ場合
#             if W >= w+AB[n][0] and K>=k+1:
#                 dp[n + 1][k+1][w+AB[n][0]] = max(dp[n + 1][k+1][w+AB[n][0]], dp[n][k][w] + AB[n][1])

dp = [[0]*(W+1) for _ in range(K+1)]
# dp = [枚数k枚を使用したときの][幅をwまで使ったときの] = 最大の重要度

#配る
for n in range(N):
    next = [[0]*(W+1) for _ in range(K+1)]
    for k in range(K+1):
        for w in range(W+1):
            next[k][w] = max(next[k][w], dp[k][w]) #選ばない場合

            # 選ぶ場合
            if W >= w+AB[n][0] and K>=k+1:
                next[k+1][w+AB[n][0]] = max(next[k+1][w+AB[n][0]], dp[k][w] + AB[n][1])

    dp = next

ans = 0
for k in dp:
    for w in k:
        ans = max(ans,w)
print(ans)