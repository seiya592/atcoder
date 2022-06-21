def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N = II()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

def dfs(n,r):
    """
    :param n:現在の頂点
    :param r: 親の頂点
    :return:
    """
    if len(E[n]) == 1:  #末端ならば
        dp[n][0] = 1
        dp[n][1] = 1
        return

    #末端でないならば潜って帰りがけに計算
    for e in E[n]:
        if e == r:
            #親は無視
            continue
        else:
            dfs(e,n)
            dp[n][0] *= sum(dp[e]) %(10**9+7)
            dp[n][1] *= dp[e][0]%(10**9+7)


E[1].append(0)

dp = [[1]*2 for _ in range(N+1)]
#dp[頂点n][0→白 1→黒] = 総数
dfs(1,0)
print(sum(dp[1])%(10**9+7))