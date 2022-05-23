def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
import math

N = II()
XY = LLIIS(N)
ans = 0
for x,y in XY:
    for x2, y2 in XY:
        t = math.sqrt((x-x2)**2 + (y-y2)**2)
        ans = max(ans,t)
print(ans)
print()