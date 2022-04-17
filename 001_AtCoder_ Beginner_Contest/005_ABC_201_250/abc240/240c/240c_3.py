def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, X = IIS()
AB = LLIIS(N)

dp = [[False] * (10000+1) for _ in range(N)]
dp[0][AB[0][0]] = True
dp[0][AB[0][1]] = True
# dp[n回目のジャンプ][座標xに到達できるか]
#配るDP

for n in range(N-1):
    for x in range(1,100*N+1):
        if dp[n][x]:
            dp[n+1][x+AB[n+1][0]] = True
            dp[n + 1][x + AB[n + 1][1]] = True
print('Yes' if dp[N-1][X] else 'No')