def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#もらうDP
N, K = IIS()
H = LIIS()

dp = [10**10] * N
dp[0] = 0
for i in range(1,N):
    for k in range(1,K+1):
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i-k] + abs(H[i]-H[i-k]))
print(dp[N-1])