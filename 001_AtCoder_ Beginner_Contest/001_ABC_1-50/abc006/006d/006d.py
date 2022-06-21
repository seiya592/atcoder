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
C = []
for _ in range(N):
    C.append(II())

dp = [INF] * N

for c in C:
    dp[bisect.bisect_left(dp,c)] = c

ans = N - bisect.bisect_left(dp,INF)
print(ans)