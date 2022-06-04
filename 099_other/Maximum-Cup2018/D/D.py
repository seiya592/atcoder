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
INF = 10**10    #INF 10**20でDP配列初期化するとTLEの原因になりうる

# https://atcoder.jp/contests/maximum-cup-2018

N, M, L, X = IIS()
A = LIIS()

dp = [[INF]*M for _ in range(N+1)]
# dp[n番目の燃料までで][i番目の休憩所に] = 何週目で行けるか
dp[0][0] = 1

for n in range(N):
    for i in range(M):
        # 燃料を使わない
        dp[n+1][i] = min(dp[n+1][i], dp[n][i])

        # 周回数を求める
        roop = (i + A[n]) // M
        # 場所を求める
        rest = (i + A[n]) % M

        dp[n+1][rest] = min(dp[n+1][rest], dp[n][i]+roop)
print('Yes' if dp[n+1][L] < X else 'No')

