"""
2022/12/10 20:46:17
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
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17
# import bisect
# class MultiSet:
#     # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
#     # multi: マルチセットか通常のOrderedSetか
#     def __init__(self, n=0, *, compress=[], multi=True):
#         self.multi = multi
#         self.inv_compress = sorted(set(compress)) if len(compress) > 0 else [i for i in range(n)]
#         self.compress = {k: v for v, k in enumerate(self.inv_compress)}
#         self.counter_all = 0
#         self.counter = [0] * len(self.inv_compress)
#         self.bit = BIT(len(self.inv_compress))
#
#     def add(self, x, n=1):     # O(log n)
#         if not self.multi and n != 1: raise KeyError(n)
#         x = self.compress[x]
#         count = self.counter[x]
#         if count == 0 or self.multi:  # multiなら複数カウントできる
#             self.bit.add(x + 1, n)
#             self.counter_all += n
#             self.counter[x] += n
#
#     def remove(self, x, n=1):  # O(log n)
#         if not self.multi and n != 1: raise KeyError(n)
#         x = self.compress[x]
#         count = self.bit.get(x + 1)
#         if count < n: raise KeyError(x)
#         self.bit.add(x + 1, -n)
#         self.counter_all -= n
#         self.counter[x] -= n
#
#     def __repr__(self):
#         return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'
#
#     def __len__(self):         # oprator len: O(1)
#         return self.counter_all
#
#     def count(self, x):        # O(1)
#         return self.counter[self.compress[x]]
#
#     def __getitem__(self, i):  # operator []: O(log n)
#         if i < 0: i += len(self)
#         x = self.bit.lower_bound(i + 1)
#         if x > self.bit.n: raise IndexError('list index out of range')
#         return self.inv_compress[x - 1]
#
#     def __contains__(self, x): # operator in: O(log n)
#         return self.bit.get(self.compress.get(x, self.bit.n) + 1, 0) > 0
#
#     def bisect_left(self, x):  # O(log n)
#         return self.bit.sum(bisect.bisect_left(self.inv_compress, x))
#
#     def bisect_right(self, x): # O(log n)
#         return self.bit.sum(bisect.bisect_right(self.inv_compress, x))

import bisect


class BIT:

    def __init__(self, len_A):
        self.N = len_A + 10
        self.bit = [0] * (len_A + 10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self, i):
        res = 0
        idx = i + 1
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self, i, x):
        idx = i + 1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self, w):
        if (w < 0):
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x


class OrderBIT:

    def __init__(self, all_values, sort_flag=False):
        if sort_flag:
            self.A = all_values
        else:
            self.A = sorted(all_values)
        self.B = BIT(len(all_values))
        self.num = 0

    def insert_val(self, x, c=1):
        k = bisect.bisect_left(self.A, x)
        self.B.update(k, c)
        self.num += c

    def delete_val(self, x, c=1):
        k = bisect.bisect_left(self.A, x)
        self.B.update(k, -c)
        self.num -= c

    # find the k-th min_val (k:0-indexed)
    def find_kth_val(self, k):
        if self.num <= k:
            ##### MINIMUM VAL #######
            return -10 ** 9
        return self.A[self.B.lower_left(k + 1)]

    # count the number of values lower than or equal to x
    def count_lower(self, x):
        if x < self.A[0]:
            return 0
        return self.B.query(bisect.bisect_right(self.A, x) - 1)

    # min_val higher than x
    def find_higher(self, x):
        return self.find_kth_val(self.count_lower(x))

"""
使い方
　　
初期化 O(NlogN)
・最終的に一度でも入る可能性のある値の配列 A
・A がsortされているならsort_flag = True

T = OrderBIT(A)




　
値の追加・削除 O(logN)
・値 x を c 個追加or削除する

T.insert_val(x,c)
T.delete_val(x,c)
　



k番目に小さい値を返す O(logN)
・kを0-indexed(0,1,2,...)
・k が全体の長さを超えている場合 MINIMUM VAL -10**9 を返す

T.find_kth_val(k)
　



値がx以下の個数を返す O(logN)

T.count_lower(x)
　



xより大きい中で最も小さい値を返す O(logN)
・存在いない場合 MINIMUM VAL -10**9 を返す

T.find_higher(x)

"""

N, M, K = IIS()
A = LIIS()



MS1 = OrderBIT(A)       #いま使っているリスト
MS2 = OrderBIT(A)       #使っていないリスト

ans = []


tot = 0
for i in range(M):
    MS2.insert_val(A[i])
for k in range(K):
    t = MS2.find_kth_val(0)
    MS1.insert_val(t)
    MS2.delete_val(t)
    tot += t
ans.append(tot)
n = 0

while n < N - M:
    f = False
    t = A[n]
    if MS2.find_higher(t-1) == t:
        # もし使っていないところにある場合は無事
        MS2.delete_val(t)
    else:
        # 使っていたら色々する
        MS1.delete_val(t)
        tot -= t
        f = True    #使っているところの数が1つ減ったフラグ
    n += 1
    MS2.insert_val(A[n+M-1])
    if not f:
        t = MS1.find_kth_val(K - 1)
        MS2.insert_val(t)
        MS1.delete_val(t)
        tot -= t
    t = MS2.find_kth_val(0)
    MS1.insert_val(t)
    MS2.delete_val(t)
    tot += t

    ans.append(tot)
print(*ans)