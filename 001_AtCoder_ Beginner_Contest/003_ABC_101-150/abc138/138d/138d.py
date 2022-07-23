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


N, Q = IIS()
E = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = IIS()
    E[a-1].append(b-1)
    E[b-1].append(a-1)

dp = [0] * N

for _ in range(Q):
    p, x = IIS()
    dp[p-1] += x

def dfs(now, last):
    if last != -1:
        dp[now] += dp[last]

    for e in E[now]:
        if e == last:
            continue
        dfs(e, now)


dfs(0,-1)
print(*dp)