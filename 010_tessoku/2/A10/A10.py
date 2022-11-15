"""
2022/10/12 23:39:58
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
S_r = [0]
for a,a_r in zip(A,reversed(A)):
    S.append(max(S[-1], a))
    S_r.append(max(S_r[-1], a_r))
S_r = list(reversed(S_r))
for _ in range(II()):
    l,r = IIS()
    print(max(S[l-1], S_r[r]))