# """
# 2022/11/19 20:56:05
# """
# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
# def LLIIS(n): return [LIIS() for _ in range(n)]
# def LI(n): return [I() for _ in range(n)]
# def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
# def YES(): print('Yes'), exit()
# def NO(): print('No'), exit()
# def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
# import sys
# sys.setrecursionlimit(500000)
# INF = 10**17
# import bisect
# class BIT:
#
#     def __init__(self, len_A):
#         self.N = len_A + 10
#         self.bit = [0] * (len_A + 10)
#
#     # sum(A0 ~ Ai)
#     # O(log N)
#     def query(self, i):
#         res = 0
#         idx = i + 1
#         while idx:
#             res += self.bit[idx]
#             idx -= idx & (-idx)
#         return res
#
#     # Ai += x
#     # O(log N)
#     def update(self, i, x):
#         idx = i + 1
#         while idx < self.N:
#             self.bit[idx] += x
#             idx += idx & (-idx)
#
#     # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
#     # O(log N)
#     def lower_left(self, w):
#         if (w < 0):
#             return -1
#         x = 0
#         k = 1 << (self.N.bit_length() - 1)
#         while k > 0:
#             if x + k < self.N and self.bit[x + k] < w:
#                 w -= self.bit[x + k]
#                 x += k
#             k //= 2
#         return x
#
# class OrderBIT:
#
#     def __init__(self, all_values, sort_flag=False):
#         if sort_flag:
#             self.A = all_values
#         else:
#             self.A = sorted(all_values)
#         self.B = BIT(len(all_values))
#         self.num = 0
#
#     def insert_val(self, x, c=1):
#         k = bisect.bisect_left(self.A, x)
#         self.B.update(k, c)
#         self.num += c
#
#     def delete_val(self, x, c=1):
#         k = bisect.bisect_left(self.A, x)
#         self.B.update(k, -c)
#         self.num -= c
#
#     # find the k-th min_val (k:0-indexed)
#     def find_kth_val(self, k):
#         if self.num <= k:
#             ##### MINIMUM VAL #######
#             return -10 ** 9
#         return self.A[self.B.lower_left(k + 1)]
#
#     # count the number of values lower than or equal to x
#     def count_lower(self, x):
#         if x < self.A[0]:
#             return 0
#         return self.B.query(bisect.bisect_right(self.A, x) - 1)
#
#     # min_val higher than x
#     def find_higher(self, x):
#         return self.find_kth_val(self.count_lower(x))
#
# H,W,N,h,w = IIS()
# A = LLIIS(H)
# T = []
# for A_ in A:
#     for a in A_:
#         T.append(a)
#
# MS = OrderBIT(T)
# for t in T:
#     MS.insert_val(t)
#
# def calc():
#     cnt = set()
#     for i in range(H*W):
#         t = MS.find_kth_val(i)
#         if t != -10 ** 9:
#             cnt.add(t)
#         else:
#             break
#     return len(cnt)
#
#
# # for i in range(H-h+1):
# #     for j in range(W-w+1):
# #         Del = []
# #         for x in range(i,i+h):
# #             for y in range(j,j+w):
# #                 MS.delete_val(A[x][y])
# #                 Del.append(A[x][y])
# #         print(calc(),' ',end='')
# #
# #         for d in Del:
# #             MS.insert_val(d)
# #     print()
#
#
# for i in range(H-h+1):
#     MS = OrderBIT(T)
#     for t in T:
#         MS.insert_val(t)
#
#     for x in range(i, i + h):
#         for y in range(0, 0 + w):
#             MS.delete_val(A[x][y])
#     print(calc(), ' ', end='')
#
#     for y in range(W-w):
#         for x in range(i,i+h):
#             MS.insert_val(A[x][y])
#             MS.delete_val(A[x][y+w])
#         print(calc(), ' ', end='')
#     print()
#
#
"""
2022/11/19 20:56:05
"""
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
import bisect
class BIT:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n: a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:                    # nは大きさ
            self.d = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f'[{l}, {r}]:{self.d[r]}')
            res.append(' '.join(res2))
            p >>= 1
        res.append(f'{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}')
        return '\n'.join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d[p] += x
            p += p & -p

    def get(self, p, default=None):     # O(log(n))
        assert p > 0
        return self.sum(p) - self.sum(p - 1) if 1 <= p <= self.n or default is None else default

    def sum(self, p):     # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d[p]
            p -= p & -p
        return res

    def lower_bound(self, x):   # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        if x <= 0: return 0
        p, r = 0, self.size
        while r > 0:
            if p + r <= self.n and self.d[p + r] < x:
                x -= self.d[p + r]
                p += r
            r >>= 1
        return p + 1

import bisect
class MultiSet:
    # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
    # multi: マルチセットか通常のOrderedSetか
    def __init__(self, n=0, *, compress=[], multi=True):
        self.multi = multi
        self.inv_compress = sorted(set(compress)) if len(compress) > 0 else [i for i in range(n)]
        self.compress = {k: v for v, k in enumerate(self.inv_compress)}
        self.counter_all = 0
        self.counter = [0] * len(self.inv_compress)
        self.bit = BIT(len(self.inv_compress))

    def add(self, x, n=1):     # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.counter[x]
        if count == 0 or self.multi:  # multiなら複数カウントできる
            self.bit.add(x + 1, n)
            self.counter_all += n
            self.counter[x] += n

    def remove(self, x, n=1):  # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.bit.get(x + 1)
        if count < n: raise KeyError(x)
        self.bit.add(x + 1, -n)
        self.counter_all -= n
        self.counter[x] -= n

    def __repr__(self):
        return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'

    def __len__(self):         # oprator len: O(1)
        return self.counter_all

    def count(self, x):        # O(1)
        return self.counter[self.compress[x]]

    def __getitem__(self, i):  # operator []: O(log n)
        if i < 0: i += len(self)
        x = self.bit.lower_bound(i + 1)
        if x > self.bit.n: raise IndexError('list index out of range')
        return self.inv_compress[x - 1]

    def __contains__(self, x): # operator in: O(log n)
        return self.bit.get(self.compress.get(x, self.bit.n) + 1, 0) > 0

    def bisect_left(self, x):  # O(log n)
        return self.bit.sum(bisect.bisect_left(self.inv_compress, x))

    def bisect_right(self, x): # O(log n)
        return self.bit.sum(bisect.bisect_right(self.inv_compress, x))

H,W,N,h,w = IIS()
A = LLIIS(H)
MS = MultiSet(N+1)
for A_ in A:
    for a in A_:
        MS.add(a)
for i in range(H-h+1):
    for x in range(i, i + h):
        for y in range(0, 0 + w):
            MS.remove(A[x][y])
    print(len(set(MS)), ' ', end='')

    for y in range(W-w):
        for x in range(i,i+h):
            MS.add(A[x][y])
            MS.remove(A[x][y+w])
        print(len(set(MS)), ' ', end='')
    print()

    for x in range(i,i+h):
        for y in range(W-w,W):
            MS.add(A[x][y])