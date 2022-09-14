"""
2022/09/08 17:32:42
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


N,U,V = IIS()

E = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)


def calc(n,d,o):

    for e in E[n]:
        if dist_A[e] != -INF:
            continue
        if o == e:
            continue

        dist_A[e] = d + 1

        calc(e,d+1,n)

def calc2(n,d,o):

    for e in E[n]:
        if dist_T[e] != -INF:
            continue
        if o == e:
            continue
        if dist_A[e] > d + 1:
            dist_T[e] = d+1
            calc2(e,d+1,n)

dist_A = [-INF] * (N+1)
dist_T = [-INF] * (N+1)

dist_A[V] = 0
calc(V,0,0)
dist_T[U] = 0
calc2(U,0,0)

max_A = -INF
ans = 0
for i in range(1,N+1):
    if max_A < dist_A[i] and dist_T[i] != -INF:
        max_A = dist_A[i]
        ans = dist_A[i] - 1

print(ans)