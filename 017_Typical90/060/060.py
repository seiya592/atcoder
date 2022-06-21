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
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LIIS()

dp = [INF] * N
up = [0] * N

for i, a in enumerate(A):
    dp[bisect.bisect_left(dp,a)] = a
    up[i] = bisect.bisect_left(dp, INF)

dp2 = [INF] * N
down = [0] * N
for i,a in enumerate(reversed(A)):
    dp2[bisect.bisect_left(dp2, a)] = a
    down[-1-i] = bisect.bisect_left(dp2, INF)

print(max([u+d-1 for u,d in zip(up, down)]))