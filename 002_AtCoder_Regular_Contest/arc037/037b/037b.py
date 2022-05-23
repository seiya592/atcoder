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

for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

done = [False] * (N+1)
done[0] = True

def dfs(n,old):
    if tmp[n]:
        return 0
    done[n] = True
    tmp[n] = True

    ret = 1
    for e in E[n]:
        if old != e:
            ret &= dfs(e,n)

    return ret

ans = 0
for n in range(1,N+1):
    tmp = [False] * (N+1)
    if not done[n]:
        ans += dfs(n,0)

print(ans)