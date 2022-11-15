"""
2022/10/12 22:44:48
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


H,W = IIS()
X = LLIIS(H)
S = [[0] * (W+1) for _ in range(H+1)]

for i,x_r in enumerate(X,start=1):
    for j,x in enumerate(x_r,start=1):
        S[i][j] += S[i-1][j] + S[i][j-1] + x - S[i-1][j-1]

for _ in range(II()):
    a,b,c,d = IIS()
    print(S[c][d] - S[a-1][d] - S[c][b-1] + S[a-1][b-1])