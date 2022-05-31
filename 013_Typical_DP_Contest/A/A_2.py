def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20



N = II()
P = LIIS()
S = sum(P)
dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

#配る
for n in range(N):
    for i in range(S):
        dp[n+1][i] += dp[n][i]
        if S >= i+P[n]:
            dp[n+1][i+P[n]] += dp[n][i]
print(sum([(i!=0) for i in dp[N]]))
