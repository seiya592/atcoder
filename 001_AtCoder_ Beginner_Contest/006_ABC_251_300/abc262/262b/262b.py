import collections


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
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

ans = 0
Q = collections.deque

def dfs(n,cnt,d):
    if cnt == 3:
        global ans
        if d in E[n]:
            ans +=1
        return

    for e in E[n]:
        if n < e:
            dfs(e,cnt+1,d)

for n in range(1,N):
    dfs(n,1,n)
print(ans)