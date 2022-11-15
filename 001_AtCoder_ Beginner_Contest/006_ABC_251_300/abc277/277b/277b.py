"""
2022/11/12 20:42:11
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


N = II()
S = []

T = set()

for _ in range(N):
    t = I()
    if t[0] in ['H','D','C', 'S']:
        pass
    else:
        NO()

    if t[1] in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        pass
    else:
        NO()

    T.add(t)

if len(T) == N:
    YES()
else:
    NO()
