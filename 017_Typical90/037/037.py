# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
# def LLIIS(n): return [LIIS() for _ in range(n)]
# def LI(n): return [I() for _ in range(n)]
# def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
# import sys
# sys.setrecursionlimit(500000)
# INF = 10**10
# class RangeMaxQuery():
#     """
#     区間更新　一点取得
#     """
#
#     def __init__(self, length, default=0):
#         self.SEG_LEN = 2 ** length.bit_length()
#         self.seg = [default] * (self.SEG_LEN * 2)
#
#     def get(self, index):
#         """
#         一点取得
#         seg木のindexの要素にvalueを追加する
#         :param index: 要素番号
#         :param value: 値
#         """
#         index += self.SEG_LEN
#         ret = self.seg[index]
#         while True:
#             index //= 2
#             if index == 0:
#                 break
#             ret = max(self.seg[index], ret)
#         return ret
#
#     def update(self, left, right, value):
#         """
#         区間最大更新
#         seg木の[left:right)の要素の最大値を更新 (valueのほうが小さい場合は更新しない)
#         :param left: 左側（含まれる）
#         :param right: 右側（含まれない）
#         """
#         left += self.SEG_LEN
#         right += self.SEG_LEN
#         while left < right:
#             if left % 2 == 1:
#                 self.seg[left] = max(value, self.seg[left])
#                 left += 1
#             if right % 2 == 1:
#                 self.seg[right - 1] = max(value, self.seg[right - 1])
#                 right -= 1
#             left //= 2
#             right //= 2
#
# W, N = IIS()
# LRV = LLIIS(N)
#
# SEG = RangeMaxQuery(W+1, -1)
# NEXT_SEG = RangeMaxQuery(W+1, -1)
# SEG.update(0,1,0)
# for n in range(N):
#
#     l, r, v = LRV[n]
#
#     for i in range(W+1):
#         # 配るDP
#
#         t = SEG.get(i)
#         # 配れない
#         if t == -1:
#             continue
#
#         # nを使わない
#         NEXT_SEG.update(i, i+1, t)
#
#         # nを使う
#         if i+l <= W:
#             NEXT_SEG.update(min(i+l, W), min(i+r+1, W+1), t + v)
#
#     SEG = NEXT_SEG
#     NEXT_SEG = RangeMaxQuery(W+1, -1)
#
# print(SEG.get(W))
