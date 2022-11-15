"""
2022/10/15 20:52:48
"""
import bisect


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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17
def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)))}
# def COMPRESS(arr):    # この関数と同等
#     *XS, = set(arr)
#     XS.sort()
#     return {e: i for i, e in enumerate(XS)}

# 一次元リスト座標復元用
def UNCOMPRESS(arr): return {i: e for i, e in enumerate(sorted(set(arr)))}

H, W, R, C = IIS()
N = II()
ROW_LIST = [0,H]
COL_LIST = [0,W]
RC = set()
for _ in range(N):
    r,c = IIS()
    ROW_LIST.append(r)
    COL_LIST.append(c)
    RC.add((r,c))
ROW_COMP = COMPRESS(set(ROW_LIST))
ROW_UNCOMP = UNCOMPRESS(set(ROW_LIST))
COL_COMP = COMPRESS(set(COL_LIST))
COL_UNCOMP = UNCOMPRESS(set(COL_LIST))
X = len(ROW_COMP)
Y = len(COL_COMP)
ROW = [[0] for _ in range(X+1)]
COL = [[0] for _ in range(Y+1)]

for r,c in RC:
    ROW[ROW_COMP[r]].append(c)
    COL[COL_COMP[c]].append(r)
for x in range(X+1):
    ROW[x].append(W+1)
    ROW[x].sort()
for y in range(Y+1):
    COL[y].append(H+1)
    COL[y].sort()

now_x = R
now_y = C

for _ in range(II()):
    d,l = IS()
    l = int(l)

    if d == 'L':
        if now_x in ROW_COMP:
            now_x = ROW_COMP[now_x]
            t = bisect.bisect_right(ROW[now_x], now_y)
            now_y = max(ROW[now_x][t-1]+1, now_y - l)
            now_x = ROW_UNCOMP[now_x]
        else:
            now_y = max(1, now_y - l)

    if d == 'R':
        if now_x in ROW_COMP:
            now_x = ROW_COMP[now_x]
            t = bisect.bisect_right(ROW[now_x], now_y)
            now_y = min(ROW[now_x][t]-1, now_y + l)
            now_x = ROW_UNCOMP[now_x]
        else:
            now_y = min(W, now_y + l)

    if d == 'U':
        if now_y in COL_COMP:
            now_y = COL_COMP[now_y]
            t = bisect.bisect_right(COL[now_y], now_x)
            now_x = max(COL[now_y][t-1]+1, now_x - l)
            now_y = COL_UNCOMP[now_y]
        else:
            now_x = max(1, now_x - l)

    if d == 'D':
        if now_y in COL_COMP:
            now_y = COL_COMP[now_y]
            t = bisect.bisect_right(COL[now_y], now_x)
            now_x = min(COL[now_y][t]-1, now_x + l)
            now_y = COL_UNCOMP[now_y]
        else:
            now_x = min(H, now_x + l)

    print(now_x, now_y)

# ROW = [[0] for _ in range(H+1)]
# COL = [[0] for _ in range(W+1)]
# for _ in range(N):
#     r,c = IIS()
#     ROW[r].append(c)
#     COL[c].append(r)
# for h in range(H+1):
#     ROW[h].append(W+1)
#     ROW[h].sort()
# for w in range(W+1):
#     COL[w].append(H+1)
#     COL[w].sort()

# now_x = R
# now_y = C
#
# for _ in range(II()):
#     d,l = IS()
#     l = int(l)
#     if d == 'L':
#         t = bisect.bisect_right(ROW[now_x], now_y)
#         now_y = max(ROW[now_x][t-1]+1, now_y - l)
#     if d == 'R':
#         t = bisect.bisect_right(ROW[now_x], now_y)
#         now_y = min(ROW[now_x][t]-1, now_y + l)
#     if d == 'U':
#         t = bisect.bisect_right(COL[now_y], now_x)
#         now_x = max(COL[now_y][t-1]+1, now_x - l)
#     if d == 'D':
#         t = bisect.bisect_right(COL[now_y], now_x)
#         now_x = min(COL[now_y][t]-1, now_x + l)

    # print(now_x,now_y)