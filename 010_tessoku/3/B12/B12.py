"""
2022/10/13 18:52:40
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

ok = 0
ng = INF

def calc(n):
    return n ** 3 + n <= N

while abs(ok-ng) > 0.001:
    mid = (ok+ng)/2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)