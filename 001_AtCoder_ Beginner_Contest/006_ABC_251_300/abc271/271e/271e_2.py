"""
2022/10/01 21:55:50
"""
import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,M,K = IIS()
ABC = LLIIS(M)
E = LIIS()
E_pos = [[] for _ in range(M+1)]
for i,e in enumerate(E,start=1):
    E_pos[e].append(i)

V = [[] for _ in range(N+1)]
for i,(a,b,c) in enumerate(ABC,start=1):
    V[a].append((c,b,i))

dist = [INF] * (N+1)
done = [False] * (N+1)
dist[1] = 0
ans = INF
def dfs(n,pos,cost):
    global ans
    if n == N:
        ans = min(ans, cost)
        done[n] = True
        return True
    ret = False
    for c,v,i in V[n]:
        j = bisect.bisect_right(E_pos[i],pos)
        if j == len(E_pos[i]):
            continue
        if dist[v] >= cost + c:
            t = dist[v]
            dist[v] = cost + c
            ret |= dfs(v,E_pos[i][j], cost+c)
            if not done[v]:
                dist[v] = t
    if ret:
        done[n] = True
    return ret

dfs(1,0,0)
print(ans if ans != INF else -1)