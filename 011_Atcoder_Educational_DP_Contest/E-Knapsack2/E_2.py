def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#配るDP
N, W = IIS()
WV = LLIIS(N)

dp = [[10**10] * (10**5+1) for _ in range(N+1)]
dp[0][0] = 0
for n in range(N):
    for v in range(10**5+1):
        wv = WV[n]
        #荷物nを受け取らない
        dp[n+1][v] = min(dp[n][v],dp[n+1][v])
        #受け取る
        if v + wv[1] <= 10**5:
            dp[n+1][v+wv[1]] = min(dp[n][v] + wv[0],dp[n+1][v+wv[1]])

ans = 10**10
for i, d in enumerate(dp[N]):
    if d <= W:
        ans = i
print(ans)