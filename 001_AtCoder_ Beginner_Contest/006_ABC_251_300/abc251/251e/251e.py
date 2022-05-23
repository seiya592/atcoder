def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

INF = 10**11
N = II()
A = LIIS()

dp = [[[INF] * 2 for _ in range(2)] for _ in range(N+1)]
#dp[餌nを][0→あげてない　1→あげた][最後の餌でまかなった]　= 値段
dp[0][0][0] = 0
dp[0][1][1] = A[-1]

for n in range(1,N+1):
    for k in range(2):
        if not (k == 1 and n == N):
            dp[n][0][k] = dp[n-1][1][k]
            dp[n][1][k] = min(dp[n-1][0][k],dp[n-1][1][k]) + A[n-1]
        else:
            dp[n][0][k] = dp[n-1][0][k]
            dp[n][1][k] = dp[n - 1][1][k]

# if A[0] < A[N-1]:
#     dp[N][1] -= A[0]
print(min(dp[N][0][0],dp[N][1][0],dp[N][0][1],dp[N][1][1]))