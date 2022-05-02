def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LIIS()
E = [[] for _ in range(N+1)]
for i in range(1,N):
    E[A[i-1]].append(i)

ans = [0] * (N)
def dfs(n):
    for e in E[n]:
        ans[e] = ans[n]+1
        dfs(e)
dfs(0)
print(max(ans))