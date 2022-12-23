"""
2022/11/19 20:55:58
"""
import collections


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
Q = II()
now = 0

D = collections.defaultdict(int)
for i in range(N):
    D[i] = A[i]

for _ in range(Q):
    q = LIIS()
    if q[0] == 1:
        x = q[1]
        now = x
        D = collections.defaultdict(int)
    elif q[0] == 2:
        i,x = q[1]-1,q[2]
        D[i] += x
    else:
        i = q[1]-1
        print(D[i] + now)
