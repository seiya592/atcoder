"""
2022/08/08 20:14:17
"""
import bisect


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


N, M = IIS()
E = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

ans = 0
for i, e in enumerate(E[1:], start=1):
    e.sort()
    if bisect.bisect_left(e, i) == 1:
        ans += 1
print(ans)