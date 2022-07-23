def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
C = IS()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

dp = [[0]*3 for _ in range(N+1)]
#dp[i番目の頂点を親とみて][0→aのみ 1→bのみ 2→ab両方]の総数

def dfs(now,old):
    if len(E[now]) == 1 and not now == 1:
        dp[now][0 if C[now-1] == 'a' else 1] = 1
        return

    if C[now - 1] == 'a':
        dp[now][0] = 1
    else:
        dp[now][1] = 1
    dp[now][2] = 1

    for e in E[now]:
        if e == old:
            continue #親

        dfs(e,now)
        if C[now-1] == 'a':
            dp[now][0] *= dp[e][0] + dp[e][2]
        else:
            dp[now][1] *= dp[e][1] + dp[e][2]

        dp[now][2] *= dp[e][0] + dp[e][1] + dp[e][2] + dp[e][2]


    dp[now][2] -= dp[now][0] if C[now - 1] == 'a' else dp[now][1]

    dp[now][0] %= 10**9+7
    dp[now][1] %= 10**9+7
    dp[now][2] %= 10**9+7

dfs(1,0)
print(dp[1][2])