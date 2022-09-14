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


N = II()
E = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)


def dfs(n,p,ans):
    """
    :param n:現在
    :param p: 親
    :param ans: 現在カウントしている距離
    :return: cnt(今の頂点の子の数) , ans(現在カウントしている距離)
    """
    cnt = 1 # 現在のノード
    ans2 = 0
    for e in E[n]:
        if p == e:
            continue    # 親
        t, tans = dfs(e, n, ans)
        ans2 += tans
        cnt += t
        ans2 += (N-t) * t
    return cnt, ans + ans2
_, ans = dfs(1,0,0)
print(ans)