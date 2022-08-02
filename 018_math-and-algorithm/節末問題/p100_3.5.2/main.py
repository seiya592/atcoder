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


import random

ans = 0
total = 1000000
for _ in range(total):
    x = random.uniform(0, 6)
    y = random.uniform(0, 9)

    if math.sqrt((3-x)**2 + (7-y)**2) <= 2.0:
        # (3,7) 半径2 の円
        ans += 1
    elif math.sqrt((3-x)**2 + (3-y)**2) <= 3.0:
        # (3.3) 半径3 の円
        ans += 1
print(ans)
