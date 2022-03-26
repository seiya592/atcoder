def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque

N = II()
E = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = IIS()
    E[a].append(b)
    E[b].append(a)

Q = deque()

Q.append(1)
dist = [-1] * (N+1)
dist[1] = 0
while len(Q) > 0:
    n = Q.popleft()
    for e in E[n]:
        if dist[e] != -1:
            continue
        dist[e] = dist[n] + 1
        Q.append(e)

max_index = dist.index(max(dist))

Q = deque()
Q.append(max_index)
dist = [-1] * (N+1)
dist[max_index] = 0

while len(Q) > 0:
    n = Q.popleft()
    for e in E[n]:
        if dist[e] != -1:
            continue
        dist[e] = dist[n] + 1
        Q.append(e)

print(max(dist) + 1)