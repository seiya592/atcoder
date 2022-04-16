def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, M = IIS()

E = [[] for _ in range(N+1)]
d = [True] * (N+1)
d[0] = False
for _ in range(M):
    x,y = IIS()
    E[x].append(y)
    d[y] = False

memo = [-1] * (N+1)
def dfs(n):
    if memo[n] != -1:
        return memo[n]
    ret = 0
    for e in E[n]:
        if memo[e] != -1:
            ret = max(ret, memo[e] + 1)
        else:
            ret = max(ret, dfs(e) + 1)

    memo[n] = ret
    return ret

ans = 0
for i,dd in enumerate(d):
    if d:
        ans = max(dfs(i), ans)
print(ans)
