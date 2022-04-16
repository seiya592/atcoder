def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
ABC = LLIIS(N)

dp = [[0] * 3 for _ in range(N+1)]
# 配るDP
for i in range(N):
    for n in range(0,3):
        dp[i+1][(n+1)%3] = max(dp[i+1][(n+1)%3], dp[i][n] + ABC[i][(n+1)%3])
        dp[i + 1][(n + 2) % 3] = max(dp[i+1][(n+2)%3],dp[i][n] + ABC[i][(n + 2) % 3])

print(max(dp[N]))