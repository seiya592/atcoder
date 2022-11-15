"""
2022/10/12 22:05:36
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
A = LIIS()

S = [0]
for a in A:
    S.append(S[-1] + a)

for _ in range(II()):
    l,r = IIS()
    if S[r] - S[l-1] > (r-l+1) - (S[r] - S[l-1]):
        print('win')
    elif S[r] - S[l-1] < (r-l+1) - (S[r] - S[l-1]):
        print('lose')
    else:
        print('draw')