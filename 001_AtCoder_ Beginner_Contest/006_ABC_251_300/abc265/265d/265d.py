"""
2022/08/21 20:49:42
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


N,P,Q,R = IIS()
A = LIIS()

# 累積和
S = [0] * (N+1)
for i, a in enumerate(A,start=1):
    S[i] = S[i-1] + a

# P を求める
def calc(l,r,c):
    while l < N:
        while r < N and S[r] - S[l] < c:
            r += 1
        if S[r] - S[l] == c:
            return r

        l += 1
    NO()

t = calc(0,1,P)
t = calc(t,t+1,Q)
t = calc(t,t+1,R)
YES()

