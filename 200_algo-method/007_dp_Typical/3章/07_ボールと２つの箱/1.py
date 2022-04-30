def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
W = LIIS()
Ws = sum(W)

dp = [[0]*(Ws+1) for _ in range(N+1)]
dp[0][0] = 1
for n in range(N):
    for w in range(Ws+1):
        dp[n+1][w] += dp[n][w]
        if w + W[n] <= Ws:
            dp[n+1][w+W[n]] += dp[n][w]
for i in range(Ws//2,Ws+1):
    if dp[N][i]:
        print(abs((Ws-i) - i))
        exit()