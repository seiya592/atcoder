"""
2022/09/12 21:15:05
"""
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
INF = 10**17


H, W = IIS()

def calc(h,w):

    ans = INF

    for i in range(1,h):
        c1 = i * w

        c2 = (h-i) * math.floor(w/2)
        c3 = (h-i) * math.ceil(w/2)

        if c1 and c2 and c3:
            ans = min(ans, max(c1,c2,c3) - min(c1,c2,c3))

        c2 = math.floor((h - i) / 2) * w
        c3 = math.ceil((h-i) / 2) * w

        if c1 and c2 and c3:
            ans = min(ans, max(c1, c2, c3) - min(c1, c2, c3))

    return ans

print(min(calc(H,W), calc(W,H)))
