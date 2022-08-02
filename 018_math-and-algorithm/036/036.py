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


A,B,H,M = IIS()

#短針
#0時を0度として角度を出す
Ha = (360 / 12) * H    # 時間だけで考える
Ha += (30 / 60) * M   # 分でも考える　1時間で30度

#短針のy座標
Ax = math.sin(math.pi * Ha / 180)
Ay = math.cos(math.pi * Ha / 180)

#単位円での割合なのでAを掛ける
Ax *= A
Ay *= A

#長針
#0分を0度として角度を出す
Ma = (360/60) * M

#長針のx座標
Bx = math.sin(math.pi * Ma / 180)
By = math.cos(math.pi * Ma / 180)

#単位円ry
Bx *= B
By *= B


#座標が求まったのでベクトルの大きさを求める
print(math.sqrt((Ax-Bx)**2 + (Ay-By)**2))
