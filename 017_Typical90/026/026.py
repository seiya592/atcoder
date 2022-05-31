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
INF = 10**20


N = II()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

done = [False] * (N+1)
group1 = []
group0 = []

def dfs(n,g):
    done[n] = True
    if g:
        group1.append(n)
    else:
        group0.append(n)

    for e in E[n]:
        if not done[e]:
            dfs(e,g^1)

dfs(1,0)
ans = group0 if len(group0) > len(group1) else group1
print(*ans[:N//2])