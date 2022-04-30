def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
ABC = LLIIS(3)

dp = [[10**10]*3 for _ in range(N)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0
for n in range(1,N):
    for i in range(3):
        for j in range(3):
            dp[n][i] = min(dp[n][i],dp[n-1][j] + abs(ABC[i][n] - ABC[j][n-1]))
print(min(dp[N-1]))