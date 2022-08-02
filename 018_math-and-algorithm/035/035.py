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


def isCircleIntersect(x1,y1,r1,x2,y2,r2):
    """
    円1と2の重なりを判定
    :param x1: 円1の中心点x
    :param y1: 円1の中心点y
    :param r1: 円1の半径
    :param x2: 円2の中心点x
    :param y2: 円2の中心点y
    :param r2: 円2の半径
    :return: 1→内側 2→内側で内接 3→重なり 4→外側で外接 5→離れている
    詳細はE8本 p.139
    """
    # 中心点間の距離を求める
    d = (x1-x2)**2 + (y1-y2)**2     # dは平方根とらないと距離ではないが計算に影響はないので二乗したまま ここで平方根取ればifの判定の二乗はいらない

    # 1. 2つの円が完全に重なっていて円周が接していないの判定
    if d < (r1-r2)**2:
        return 1

    # 2. 2つの円が完全に重なっていて円周が接している判定
    if d == (r1-r2)**2:
        return 2

    # 3. 2つの円が互いに交差する判定 （重なっており、接している部分が2か所ある）
    if (r1-r2)**2 < d < (r1+r2)**2: #(r1-r2)は上の2つの判定があればいらないが公式はこう。
        return 3

    # 4. 2つの円が重なっていないが、接している判定
    if d == (r1+r2)**2:
        return 4

    # 5. 2つの円が重なっておらず、接していない判定
    if d > (r1+r2) ** 2:    # ここは最後のパターンなので判定なくてもいい
        return 5



x1,y1,r1 = IIS()
x2,y2,r2 = IIS()
print(isCircleIntersect(x1,y1,r1,x2,y2,r2))
