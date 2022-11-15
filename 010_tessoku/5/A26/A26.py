"""
2022/10/26 18:30:34
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

ALL = (10 **5) * 3
A = [0] * (ALL+1)

for i in range(2,ALL+1):
    if A[i]:
        continue
    j = 2
    while i*j <= ALL:
        A[i*j] = 1
        j += 1

for _ in range(II()):
    if A[II()]:
        print('No')
    else:
        print('Yes')