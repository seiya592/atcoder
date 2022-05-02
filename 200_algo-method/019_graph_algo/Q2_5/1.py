def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
P = LIIS()
E = [[] for _ in range(N+1)]

for i in range(1,N):
    E[P[i-1]].append(i)

ans = [0] * N
def dfs(n):
    ret = 0
    for e in E[n]:
        ret += dfs(e) + 1
    ans[n] = ret
    return ret
dfs(0)
for a in ans:
    print(a)
