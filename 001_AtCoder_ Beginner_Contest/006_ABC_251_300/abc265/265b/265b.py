"""
2022/08/21 20:49:32
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, M, T = IIS()
A = LIIS()

B = [0] * (N+1)
for _ in range(M):
    x,y = IIS()
    B[x] = y

for i in range(1, N):
    T -= A[i-1]
    if T <= 0:
        NO()
    T += B[i+1]



YES()
