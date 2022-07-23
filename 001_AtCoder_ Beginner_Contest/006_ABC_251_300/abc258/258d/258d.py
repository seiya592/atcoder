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
INF = 10**30


N,X = IIS()
AB = LLIIS(N)
ans = INF
def dfs(n,time,cnt):
    # n番目のステージ
    global ans
    if cnt == X or n == N:
        return
    #絶対にストーリも1回は見る
    t = time + AB[n][0] + AB[n][1]
    c = cnt + 1

    #このステージのみでゲームを終わらせる
    tt = t + ((X - c) * AB[n][1])

    #更新
    ans = min(ans,tt)

    dfs(n+1, t, c)

dfs(0,0,0)
print(ans)