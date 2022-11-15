"""
2022/09/17 20:39:24
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
INF = 10**17


S = LI(10)

row_min = INF
row_max = -1
col_max = -1
col_min = INF
for i,S_ in enumerate(S):
    for j,s in enumerate(S_):
        if s == '#':
            row_max = max(i,row_max)
            row_min = min(i,row_min)
            col_max = max(j,col_max)
            col_min = min(j,col_min)
print(row_min+1,row_max+1)
print(col_min+1,col_max+1)
