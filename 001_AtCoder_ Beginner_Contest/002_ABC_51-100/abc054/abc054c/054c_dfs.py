def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
E = [[] for _ in range(N)]
for _ in range(M):
    a,b = IIS()
    E[b-1].append(a-1)
    E[a-1].append(b-1)

check = [False] * N
ans = 0
check[0] = True
def dfs(i):
    global ans
    if all(check):
        ans += 1
        return 0
    for e in E[i]:
        if not check[e]:
            check[e] = True
            dfs(e)
            check[e] = False

dfs(0)
print(ans)