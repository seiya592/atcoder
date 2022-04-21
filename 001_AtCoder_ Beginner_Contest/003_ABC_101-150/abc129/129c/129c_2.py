def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, M = IIS()
ng = [False] * N
for _ in range(M):
    a = II()
    ng[a-1] = True

dp = [0] * N
dp[0] = 1 if not ng[0] else 0
if N == 1:
    print(dp[0])
    exit()
dp[1] = (1 + dp[0]) if not ng[1] else 0
#もらうDP
for n in range(2, N):
    if not ng[n]:
        dp[n] = (dp[n-1] + dp[n-2]) % (10**9+7)
print(dp[N-1] % (10**9+7))
