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


ax, ay = IIS()
bx, by = IIS()
cx, cy = IIS()

# 内積によるなす角で角度判定

# 1, bを中心として判定

# ベクトルを算出
BAx = ax - bx
BAy = ay - by
BCx = cx - bx
BCy = cy - by

# 内積を求める
S = BAx*BCx + BAy*BCy
if S <= 0:
    print(math.sqrt((BAx)**2 + (BAy) ** 2))
    exit()

# 2, cを中心として判定
CAx = ax - cx
CAy = ay - cy
CBx = bx - cx
CBy = by - cy
# 内積を求める
S = CAx*CBx + CAy*CBy
if S <= 0:
    print(math.sqrt((CAx)**2 + (CAy)**2))
    exit()


# 角ABC　角ACBが共に90度以下の場合
print(abs((CAx*CBy) - (CAy*CBx)) / math.sqrt((CBx)**2 + (CBy)**2))
