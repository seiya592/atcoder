"""
2022/08/21 20:49:37
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


H,W = IIS()
G = LI(H)

nowx = 0
nowy = 0

done = [[False] * W for _ in range(H)]

while True:
    if done[nowx][nowy]:
        print(-1)
        exit()
    done[nowx][nowy] = True

    if G[nowx][nowy] == 'U' and nowx != 0:
        nowx -= 1
    elif G[nowx][nowy] == 'D' and nowx != H-1:
        nowx += 1
    elif G[nowx][nowy] == 'L' and nowy != 0:
        nowy -=1
    elif G[nowx][nowy] == 'R' and nowy != W-1:
        nowy += 1
    else:
        print(nowx+1,nowy+1)
        exit()