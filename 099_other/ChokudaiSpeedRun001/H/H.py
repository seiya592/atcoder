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


# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_h

N = II()
A = LIIS()

dp = [INF] * N

for a in A:
    dp[bisect.bisect_right(dp,a)] = a

print(bisect.bisect_left(dp,INF))
