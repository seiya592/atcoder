def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#もらうDP
N, W = IIS()
WV = LLIIS(N)

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(W+1):
        wv = WV[i-1]
        #荷物を受け取らない
        dp[i][w] = max(dp[i][w] ,dp[i-1][w])
        #受け取る
        dp[i][w] = max(dp[i][w], dp[i-1][w-wv[0]] + wv[1] if w-wv[0] >= 0 else 0)
print(max(dp[N]))