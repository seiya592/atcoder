"""
2022/10/01 20:39:20
"""
import heapq


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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,M,K = IIS()
ABC_o = LLIIS(M)
E = LIIS()
# S = set()
# for k in range(K-1):
#     S.add((E[k],E[k+1]))

S = [set() for _ in range(N+1)]
for k in range(K-1):
    S[E[k]].add(E[k+1])

E = [[] for _ in range(N+1)]

for a,b,c in ABC_o:
    if (a,b) in S:
        E[a].append((c,b))

Q = []
heapq.heapify(Q)
dist = [-INF] * (N+1)
done = [False] * (N+1)
Q.append((0,1))

while Q:
    d,n = heapq.heappop(Q)
    if done[n]:
        continue

    done[n] = True

    for c,e in E[n]:

        if dist[e] == -INF or dist[e] > dist[n] + c:
            dist[e] = dist[n] + c
            heapq.heappush(Q,(dist[e], e))
if dist[N] == -INF:
    print(-1)
else:
    print(dist[N])