import math


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


T = II()
L,X,Y = IIS()

def calc(e):
    x = 0
    y = math.sin(math.pi * 2 * e / T) * -(L / 2)
    z = math.cos(math.pi * 2 * e / T) * -(L / 2) + (L/2)

    ay = math.sqrt((0-X)**2 + (y-Y)**2)
    ans = math.atan2(z, ay) * (180 / math.pi)
    return ans

Q = II()
for _ in range(Q):
    print(calc(II()))