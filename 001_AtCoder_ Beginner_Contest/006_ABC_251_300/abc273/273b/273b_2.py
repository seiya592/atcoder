"""
2022/10/15 23:44:56
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


X, K = IIS()

for k in range(1,K+1):
    t = X % (10**k) // (10**(k-1))
    if t >= 5:
        X = (X // (10**k) + 1) * (10 ** k)
    else:
        X = (X // (10**k)) * (10 ** k)
print(X)