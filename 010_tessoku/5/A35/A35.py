"""
2022/11/16 20:22:01
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

for i in range(N-1,0,-1):
    tmp = []
    if i%2:
        for j in range(0,i):
            tmp.append(max(A[j],A[j+1]))
    else:
        for j in range(0,i):
            tmp.append(min(A[j], A[j + 1]))
    A = tmp

print(A[0])