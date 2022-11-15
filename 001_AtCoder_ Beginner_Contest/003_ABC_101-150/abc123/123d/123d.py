"""
2022/09/26 17:27:07
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


X,Y,Z,K = IIS()
A = LIIS()
B = LIIS()
C = LIIS()

T = [a + b for b in B for a in A]

if X*Y > K:
    T.sort(reverse=True)
    T = T[:K]

ans = [t+c for t in T for c in C]

ans.sort(reverse=True)

for a in ans[:K]:
    print(a)
