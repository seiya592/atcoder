def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

# 解説AC

N = II()
DCS = [LIIS() for _ in range(N)]

DCS.sort()
MAX_TIME = DCS[N-1][0] + 1
dp = [[0] * MAX_TIME for _ in range(N+1)]

for i, DCS in enumerate(DCS, start=1):
    d, c, s = DCS
    for j in range(MAX_TIME):
        if j < c or d < j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + s)

print(max(dp[N]))