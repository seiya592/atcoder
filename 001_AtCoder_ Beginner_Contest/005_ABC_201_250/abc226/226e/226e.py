"""
2022/08/26 17:13:38
"""
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, M = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

done = [False] * (N+1)
def dfs(n):
    done[n] = True

    n_cnt = 1
    e_cnt = len(E[n])
    for e in E[n]:
        if done[e]:
            continue
        cnt1, cnt2 = dfs(e)
        e_cnt += cnt2
        n_cnt += cnt1

    return n_cnt, e_cnt

ans = 1
flg = False
for i in range(1,N+1):
    if done[i]:
        continue
    a,b = dfs(i)

    if a*2 == b:
        ans *= 2
        ans %= 998244353
    else:
        flg = True
print(ans if not flg else 0)