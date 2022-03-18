def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
P = [[] for _ in range(N+1)]

for i in range(1,N+1):
    p = II()
    if p != -1:
        P[p].append(i)
    else:
        CEO = i

M = II()
Q = [[] for _ in range(N+1)]
for i in range(M):
    a, b = IIS()
    Q[a].append([i, b])


boss = [False] * (N + 1)
ans = [False] * M
def dfs(i):
    # クエリ処理
    for q in Q[i]:
        if boss[q[1]]:
            ans[q[0]] = True
        else:
            ans[q[0]] = False

    boss[i] = True
    for p in P[i]:
        dfs(p)
    boss[i] = False


dfs(CEO)

for a in ans:
    if a:
        print('Yes')
    else:
        print('No')