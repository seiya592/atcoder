"""
2022/10/13 18:37:20
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


N, X = IIS()
A = LIIS()

ok = 0
ng = N


def calc(n):
    return A[n] <= X


while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok+1)