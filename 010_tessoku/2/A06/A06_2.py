"""
2022/10/12 22:02:43
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


N,Q = IIS()
A = LIIS()
S = [0] * (N+1)
for i,a in enumerate(A,start=1):
    S[i] = S[i-1] + a
for _ in range(Q):
    l,r = IIS()
    print(S[r]-S[l-1])
