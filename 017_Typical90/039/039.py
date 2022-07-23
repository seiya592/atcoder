import collections


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
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

child = [-1] * (N+1)
child[1] = 0
def dfs(n,o):
    tmp = 1
    for e in E[n]:
        if e == o:
            continue

        tmp += dfs(e,n)

    child[n] = tmp
    return tmp

dfs(1,0)

ans = 0
for c in child[1:]:
    ans += c * (N-c)
print(ans)
