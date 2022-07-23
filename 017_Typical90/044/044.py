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


N, Q = IIS()
A = LIIS()
now = 0

for _ in range(Q):
    t,x,y = IIS()
    x -= 1
    y -= 1

    if t == 1:
        A[(x+now)%N], A[(y+now)%N] = A[(y+now)%N], A[(x+now)%N]
    elif t == 2:
        if now:
            now -= 1
        else:
            now = N-1
    else:
        print(A[(x+now)%N])
