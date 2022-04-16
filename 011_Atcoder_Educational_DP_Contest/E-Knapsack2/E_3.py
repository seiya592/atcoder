def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#もらうDP
N, W = LIIS()
WV = LLIIS(N)

dp = [[10**10+1] * (10**5+1) for _ in range(N+1)]
dp[0][0] = 0
for n in range(1,N+1):
    for v in range(10**5+1):
        wv = WV[n-1]
        #受け取らない
        dp[n][v] = min(dp[n-1][v],dp[n][v])
        #受け取る
        if v-wv[1] >= 0:
            dp[n][v] = min(dp[n][v], dp[n-1][v-wv[1]] + wv[0])

for i,d in enumerate(dp[N]):
    if d <= W:
        ans = i
print(ans)