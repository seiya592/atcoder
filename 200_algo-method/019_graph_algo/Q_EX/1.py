def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
E = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    f,s = IIS()
    E[f].append(s)
    deg[s] += 1

from collections import deque
Q = deque()
for i,d in enumerate(deg):
    if not d:
        Q.append(i)

while len(Q) > 0:
    n = Q.popleft()

    for e in E[n]:
        deg[e] -= 1
        if not deg[e]:
            Q.append(e)

for d in deg:
    if d:
        print('No')
        exit()
print('Yes')