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

N, M, K= IIS()

dp = [[0]*(M+1) for _ in range(N)]
for i in range(M+1):
    dp[0][i] = i

for n in range(1,N):
    for i in range(1,M+1):
        MAX = min(M,i+K-1) if K > 0 else 0
        MIN = max(0,i-K if K > 0 else 0)
        dp[n][i] = (dp[n-1][M]-dp[n-1][MAX]+dp[n-1][MIN]+dp[n][i-1]) % 998244353

print(dp[N-1][M])