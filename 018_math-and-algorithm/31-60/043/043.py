"""
2022/08/08 19:58:53
"""
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
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

done = [False] * (N+1)
done[0] = True
done[1] = True
Q = collections.deque()
Q.append(1)

while Q:
    n = Q.popleft()

    for e in E[n]:
        if done[e]:
            continue
        done[e] = True
        Q.append(e)

print('The graph is connected.' if all(done) else 'The graph is not connected.')