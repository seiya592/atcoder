import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20


N = II()
W = []
for _ in range(N):
    W.append(II())

ans = [-1]
for w in W:
    if ans[-1] < w:
        ans.append(w)
    else:
        ans[bisect.bisect_left(ans, w)] = w
print(len(ans)-1)