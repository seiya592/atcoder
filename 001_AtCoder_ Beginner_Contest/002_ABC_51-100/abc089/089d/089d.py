"""
2022/09/21 16:58:08
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


H,W,D = IIS()
A = LLIIS(H)
E = [0] * (H*W+1)
for i,aa in enumerate(A,start=1):
    for j, a in enumerate(aa,start=1):
        E[a] = (i,j)


S = [[0] for _ in range(D)]
for d in range(D):
    if d:
        now = d
        o_i,o_j = E[now]
    else:
        now = D
        S[d].append(0)
    o_i, o_j = E[now]
    while now + D <= H*W:
        now += D
        i,j = E[now]
        S[d].append(abs(o_i-i)+abs(o_j-j) + S[d][-1])
        o_i = i
        o_j = j

Q = II()
for _ in range(Q):
    l,r = IIS()
    mod = l % D
    print(S[mod][r//D] - S[mod][(l//D)])