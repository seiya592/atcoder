
"""
自作 動作はするけど遅い?
"""
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
