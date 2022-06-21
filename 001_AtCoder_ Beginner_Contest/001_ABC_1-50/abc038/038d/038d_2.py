import bisect


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
INF = 10**10


N = II()
WH = LLIIS(N)

WH.sort(key=lambda x:(x[0],-x[1]))

dp = [INF] * N
for _,h in WH:
    dp[bisect.bisect_left(dp,h)] = h

print(bisect.bisect_left(dp,INF))
