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


N, W = IIS()
WV = LLIIS(N)

#
dp = [-INF] * (W*2)
dp[0] = 0

for n in range(N):
    w,v = WV[n]
    for i in reversed(range(W)):
        if dp[i] == -INF:
            continue
        dp[i+w] = max(dp[i+w], dp[i] + v)
print(max(dp[:W+1]))