"""
2022/10/12 22:14:59
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


D = II()
N = II()
S = [0] * (D+2)
for _ in range(N):
    l,r = IIS()
    S[l] += 1
    S[r+1] += -1
for i in range(1,D+1):
    S[i] += S[i-1]
for s in S[1:D+1]:
    print(s)
