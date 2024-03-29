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


N = II()
x,y = IIS()
x2,y2 = IIS()



# 対角線の半分の長さを求める
r = math.sqrt((x-x2) ** 2 + (y-y2) ** 2) / 2

# 中心のx,y座標
d0 = math.atan2((y2-y), (x2-x))
xc = math.cos(d0) * r + x
yc = math.sin(d0) * r + y

# 角度を求める
# 中心から見たp0の角度を求める
p0d = math.atan2(y-yc,x-xc)
# p0からp1の角度
d = 2 * math.pi / N

p1d = p0d + d

ansx = math.cos(p1d) * r + xc
ansy = math.sin(p1d) * r + yc
print(ansx,ansy)
