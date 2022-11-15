"""
2022/10/12 23:05:03
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


H,W,N = IIS()
S = [[0]*(W+2) for _ in range(H+2)]
for _ in range(N):
    a,b,c,d = IIS()
    S[a][b] += 1
    S[a][d+1] -= 1
    S[c+1][b] -= 1
    S[c+1][d+1] += 1

for i in range(1,H+1):
    for j in range(1,W+1):
        S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]
for s in S[1:H+1]:
    print(*s[1:W+1])