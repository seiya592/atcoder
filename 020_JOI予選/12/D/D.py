def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [II() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20

# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

D, N = IIS()

T = LI(D)
ABC = LLIIS(N)
# E = [[] for _ in range(D)]
#
# for i in range(D):
#     a,b,c = IIS()
#     if a<=T[i]<=b:
#         E[i].append(c)

dp = [[-1]*N for i in range(D)]
#dp[n日目][服iを着た時の] = 派手さの最大値
for i in range(N):
    if ABC[i][0] <= T[0] <= ABC[i][1]:
        # dp[0][i] = ABC[i][2]
        dp[0][i] = 0

for n in range(1,D):
    for i in range(N):  #今日着ようとしている 服
        a, b, c = ABC[i]
        if not(a<=T[n]<=b):
            continue
        for j in range(N):  #昨日来てた服
            if dp[n-1][j] == -1:    #-1は昨日きれなかった服
                continue
            dp[n][i] = max(dp[n][i],dp[n-1][j] + abs(ABC[j][2] - c))
print(max(dp[-1]))
