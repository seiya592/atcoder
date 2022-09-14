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
def cross(x1,y1,x2,y2):
    """
    ベクトル(x1,y1)と(x2,y2)の外積の大きさ
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return: 大きさ（絶対値が大きさになる）
    """
    return x1*y2 - x2*y1


#1つ目の線分の両端
x1,y1 = IIS()
x2,y2 = IIS()

#2つめの線分の両端
x3,y3 = IIS()
x4,y4 = IIS()


#１つめの線分のx1y1を中心とする外積を求める
a1 = cross(x2-x1, y2-y1, x3-x1, y3-y1)
a2 = cross(x2-x1, y2-y1, x4-x1, y4-y1)

#2つめの線分のx3y3を中心とする外積を求める
a3 = cross(x4-x3, y4-y3, x1-x3, y1-y3)
a4 = cross(x4-x3, y4-y3, x2-x3, y2-y3)

if a1 == a2 == a3 == a4 == 0:
    # x軸だけで考える
    if not x1 == x2 == x3 == x4:
        x1,x2 = min(x1,x2), max(x1,x2)
        x3, x4 = min(x3, x4), max(x3, x4)

        if min(x2,x4) >= max(x1,x3):
            YES()


    # y軸だけで考える
    if not y1 == y2 == y3 == y4:
        y1, y2 = min(y1, y2), max(y1, y2)
        y3, y4 = min(y3, y4), max(y3, y4)

        if min(y2, y4) >= max(y1, y3):
            YES()

    NO()



else:
    if (a1 <= 0 <= a2 or a2 <= 0 <= a1) and (a3 <= 0 <= a4 or a4 <= 0 <= a3):
        YES()

    NO()