def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)

#解説AC
N, M = IIS()

E = [[] for _ in range(N+1)]
Er = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = IIS()
    E[a].append(b)
    Er[b].append(a)



def dfs(n):
    done[n] = True

    for e in E[n]:
        if not done[e]:
            dfs(e)

    rank.append(n)

def dfs2(n):
    tmp = 0
    done[n] = True

    for e in Er[n]:
        if not done[e]:
            tmp += dfs2(e)

    return tmp + 1


done = [False] * (N+1)
rank = []
for i in range(1, N+1):
    if not done[i]:
        dfs(i)

ans = 0
done = [False] * (N+1)
for r in reversed(rank):
    if not done[r]:
        tmp = dfs2(r)
        ans += (tmp*(tmp-1))//2

print(ans)