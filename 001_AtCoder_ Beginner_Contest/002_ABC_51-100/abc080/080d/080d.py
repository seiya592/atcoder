"""
2022/10/26 17:42:57
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


N,C = IIS()
STC = LLIIS(N)

A = [[0]*(10**5+2) for _ in range(C+1)]

for s,t,c in STC:
    A[c][s] += 1
    A[c][t] -= 1

for c in range(1,C+1):
    for i in range(1,10**5+2):
        if A[c][i] < 0:
            A[0][i+1] += A[c][i]
        else:
            A[0][i] += A[c][i]

for i in range(1,10**5+2):
    A[0][i] += A[0][i-1]
print(max(A[0]))