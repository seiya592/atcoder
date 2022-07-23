def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,Q = IIS()
S = I()

now = 0
for _ in range(Q):
    n,x = IIS()
    if n == 1:
        if now - x < 0:
            now = N + (now - x)
        else:
            now -= x
    else:
        t = (now + (x-1)) % N
        print(S[t])
