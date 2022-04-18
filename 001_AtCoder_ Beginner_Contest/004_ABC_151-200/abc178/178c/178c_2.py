def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
dp = [[[0] * 2 for _ in range(2)] for _ in range(N+1)]
dp[0][0][0] = 1
#dp[n桁目][0:0が無い 1:0が存在][0:9が無い 1:9が存在]
for n in range(1,N+1):
    for n1 in range(2):
        for n9 in range(2):
            for t in range(10):
                dp[n][n1|(t==1)][n9|(t==9)] += dp[n-1][n1][n9] % (10**9+7)
print(dp[N][1][1]%(10**9+7))
