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


# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
N,M = IIS()
D = []
C = []

for i in range(N):
    D.append(II())
for i in range(M):
    C.append(II())

dp = [[INF]*(N+1) for _ in range(M+1)]
# dp[d][n] = d日目にn都市に到着できる最小疲労度
for i in range(M+1):
    dp[i][0] = 0
for d in range(1,M+1):
    for n in range(1, N+1):
        dp[d][n] = min(dp[d-1][n], dp[d-1][n-1] + D[n-1]*C[d-1])
print(dp[-1][-1])