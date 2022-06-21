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
#自力AC

N = II()

dp = [INF] * N

#単調増加でないといけない　→　単調減少(または同値)になってしまう要素数を求める
for _ in range(N):
    a = -II()
    dp[bisect.bisect_right(dp, a)] = a
print(bisect.bisect_left(dp,INF))
