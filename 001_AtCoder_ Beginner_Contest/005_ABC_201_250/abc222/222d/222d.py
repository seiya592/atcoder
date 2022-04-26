def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LIIS()
B = LIIS()
dp = [[0] * (3001) for _ in range(N+1)]
for i in range(3001):
    dp[0][i] = 1
for n in range(1,N+1):
    for v in range(3001):
        if A[n-1] <= v <= B[n-1]:
            if v == 0:
                dp[n][v] = dp[n-1][v]
            else:
                dp[n][v] = (dp[n-1][v] + dp[n][v-1])%998244353
        else:
            if v == 0:
                dp[n][v] = 0
            else:
                dp[n][v] = dp[n][v-1]
print(dp[N][3000])