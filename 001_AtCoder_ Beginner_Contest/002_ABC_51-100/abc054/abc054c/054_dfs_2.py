def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]

#15m 自力AC

N, M = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = IIS()
    E[b].append(a)
    E[a].append(b)

done = [False] * (N+1)
done[1] = True
def dfs(n,i):
    if n == N:
        return 1
    ret = 0
    for e in E[i]:
        if not done[e]:
            done[e] = True
            ret += dfs(n+1,e)
            done[e] = False
    return ret

print(dfs(1,1))