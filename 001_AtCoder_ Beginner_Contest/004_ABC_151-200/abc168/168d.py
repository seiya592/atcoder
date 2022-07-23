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


N,M = IIS()
E = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

Q = collections.deque()
Q.append(1)

dist = [INF] * (N+1)
ans = [0] * (N+1)

dist[1] = 0
while Q:
    n = Q.popleft()

    for e in E[n]:
        if dist[e] == INF:
            ans[e] = n
            dist[e] = dist[n] + 1
            Q.append(e)

if 0 in ans[2:]:
    print('No')
else:
    print('Yes')
    for a in ans[2:]:
        print(a)