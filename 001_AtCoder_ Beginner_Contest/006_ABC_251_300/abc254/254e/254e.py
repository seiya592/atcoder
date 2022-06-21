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
sys.setrecursionlimit(100000)
INF = 10**10

def solve(X, K):
    q = collections.deque()
    q.append([X, 0])
    ans = X
    done = set()
    done.add(X)
    while q:
        x, k = q.popleft()
        if k < K:
            for e in E[x]:
                if not e in done:
                    done.add(e)
                    ans += e
                    q.append([e,k+1])
    return ans




N, M = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

Q = II()
for _ in range(Q):
    x,k = IIS()
    print(solve(x,k))