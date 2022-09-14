"""
2022/08/08 20:26:44
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
    a, b = IIS()
    E[a].append(b)
    E[b].append(a)

C = [-1] * (N+1)


def calc(t):
    Q = collections.deque()
    Q.append(t)
    C[t] = 0
    while Q:
        n = Q.popleft()

        for e in E[n]:
            if C[e] == -1:
                C[e] = 1 ^ C[n]
                Q.append(e)
            else:
                if C[e] == C[n]:
                    NO()

for i in range(1,N+1):
    if C[i] == -1:
        calc(i)

if all([(c >= 0) for c in C[1:]]):
    YES()
else:
    NO()
