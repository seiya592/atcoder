def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


H, W, M = IIS()
ob = [[True] * W for _ in range(H)]
ans = [[0] * W for _ in range(H)]
for _ in range(M):
    x, y = IIS()
    ob[x-1][y-1] = False


def dfs(x,y,row,sec):
    if ans[x][y] == 1:
        if not(x==0 and y==0):
            return

    ans[x][y] = 1
    if row:
        if x+1<H and ob[x+1][y]:
            dfs(x+1,y,True,False)
        if y+1<W and not sec and ob[x][y+1]:
            dfs(x,y+1,False,True)

    else:
        if y+1<W and ob[x][y+1]:
            dfs(x,y+1,False,False)
        if x+1<H and not sec and ob[x+1][y]:
            dfs(x+1,y,True,True)


dfs(0,0,True,False)
dfs(0,0,False,False)

t = 0
for a in ans:
    t += sum(a)
print(t)