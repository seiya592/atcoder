def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20
import bisect

N = II()
WH = LLIIS(N)

WH.sort(key=lambda x:(x[0],-x[1]))

# 横を昇順にしたことで WH[i] <= WH[i+1] になる。
# これにより横が原因で　i以降の箱が被せれないということがなくなる。

# 横が同じ場合、縦を降順にすることで、同じ横の長さの箱にかぶせることがなくなる。
LIS = [0]
for _, h in WH:
    if LIS[-1] < h:
        LIS += [h]
    else:
        LIS[bisect.bisect_left(LIS,h)] = h
print(len(LIS)-1)