"""
2022/08/09 21:39:04
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


H, W = IIS()
A = LLIIS(H)

HA = [0] * H
WA = [0] * W

for h in range(H):
    t = 0
    for w in range(W):
        t += A[h][w]
    HA[h] = t

for w in range(W):
    t = 0
    for h in range(H):
        t += A[h][w]
    WA[w] = t

ans = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = HA[i] + WA[j] - A[i][j]

for a in ans:
    print(*a)