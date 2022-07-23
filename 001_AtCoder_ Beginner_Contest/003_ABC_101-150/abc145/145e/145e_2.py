def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, T = IIS()
AB = LLIIS(N)

dp = [[-INF] * T for _ in range(N+1)]
dpr = [[-INF] * T for _ in range(N+1)]
dp[0][0] = 0
dpr[0][0] = 0

for n in range(1,N+1):
    for i in range(T):
        dp[n][i] = max(dp[n-1][i], dp[n][i], dp[n][max(0,i-1)])
        dpr[n][i] = max(dpr[n - 1][i], dpr[n][i], dpr[n][max(0, i - 1)])

        if i - AB[n-1][0] >= 0:
            dp[n][i] = max(dp[n-1][i-AB[n-1][0]] + AB[n-1][1], dp[n][i])
        if i - AB[-n][0] >= 0:
            dpr[n][i] = max(dpr[n-1][i-AB[-n][0]] + AB[-n][1], dpr[n][i])

ans = 0
for n in range(N):
    for i in range(T):
        ans = max(ans, dp[n][i] + dpr[N-n-1][T-i-1] + AB[n][1])
print(ans)
