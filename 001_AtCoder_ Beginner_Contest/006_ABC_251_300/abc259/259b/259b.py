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
import math

a,b,d = IIS()

# theta = math.radians(d)
theta = d * math.pi / 180
x = math.cos(theta) * a - math.sin(theta) * b
y = math.cos(theta) * b + math.sin(theta) * a
print(x,y)