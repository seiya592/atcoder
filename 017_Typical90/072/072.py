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


H, W = IIS()
C = LI(H)

def dfs(i,j,dist,start):
    if dist != 0 and (i,j) == start:
        return dist

    ans = -1
    for x,y in PLUS(i,j):
        if 0<=x<H and 0<=y<W:
            if C[x][y] != '#':
                if not done[x][y]:
                    done[x][y] = True
                    ans = max(ans,dfs(x,y,dist+1,start))
                    done[x][y] = False
    return ans



done = [[False] * W for _ in range(H)]
ans = -1
for i in range(H):
    for j in range(W):
        if C[i][j] != '#':
            ans = max(dfs(i,j,0,(i,j)),ans)
print(ans if ans >= 3 else -1)