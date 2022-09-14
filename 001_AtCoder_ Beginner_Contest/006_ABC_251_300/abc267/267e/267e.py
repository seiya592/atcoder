"""
2022/09/03 20:35:29
"""
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
INF = 10**17


N,M = IIS()
A = LIIS()
E = [[] for _ in range(N+1)]
L = [0] * (N+1)
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    L[u] += A[v-1]
    E[v].append(u)
    L[v] += A[u-1]

import heapq
Q = []
for i,l in enumerate(L[1:], start=1):
    Q.append((l,i))
done = [0] * (N+1)
heapq.heapify(Q)
t = 0
ans = -INF
while t < N:
    l,i = heapq.heappop(Q)
    if done[i]:
        continue
    ans = max(ans, l)
    for e in E[i]:
        if done[e]:
            # なくても通る
            continue
        L[e] -= A[i-1]
        heapq.heappush(Q,(L[e], e))

    done[i] = 1
    t += 1
print(ans)