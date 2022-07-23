import collections


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
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0
def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

H, W = IIS()
P = LLIIS(H)

#bit全探索
ALL = 2 ** H
ans = 0

for n in range(1,ALL):
    d = collections.defaultdict(int)
    for j in range(W):
        s = set(P[i][j] for i in range(H) if has_bit(n,i))
        if len(s) == 1:
            d[s.pop()] += 1

    d = dict(d)
    if d:
        ans = max(ans, popcount(n) * max(d.values()))
print(ans)

# for n in range(1, ALL):
#     done = set()
#     for j in range(W):
#         target = set()
#         for i in range(H):
#             if not has_bit(n,i):
#                 continue
#             target.add(P[i][j])
#         if len(target) > 1:
#             continue
#         t = target.pop()
#         if t in done:
#             continue
#         done.add(t)
#
#         cnt = 1
#         for k in range(j+1,W):
#             for i in range(H):
#                 if not has_bit(n, i):
#                     continue
#                 if P[i][k] != t:
#                     break
#             else:
#                 cnt += 1
#         ans = max(ans,popcount(n) * cnt)
#
# print(ans)