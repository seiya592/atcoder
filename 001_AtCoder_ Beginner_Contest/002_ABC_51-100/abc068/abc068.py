def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque

N, M = IIS()
E = [[] for i in range(N)]
for _ in range(M):
    a,b = IIS()
    E[a-1].append(b-1)
    E[b-1].append(a-1)

Q = deque()
Q.append(0)
cost = [-1] * N
cost[0] = 0
while len(Q) > 0:
    i = Q.popleft()
    for e in E[i]:
        if cost[e] == -1:
            Q.append(e)
            cost[e] = cost[i] + 1

if cost[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')