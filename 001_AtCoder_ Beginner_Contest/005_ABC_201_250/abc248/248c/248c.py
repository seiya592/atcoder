def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, M, K = IIS()
#dp[長さiの時][数値の合計MAX2500]
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N+1):
    for j in range(K+1):
        for m in range(1,M+1):
            if j+m <= K:
                dp[i][j+m] += dp[i-1][j]
                dp[i][j+m] %= 998244353

ans = 0
for d in dp[N]:
    ans += d
    ans %= 998244353
print(ans)

