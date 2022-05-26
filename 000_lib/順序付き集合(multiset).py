# https://juppy.hatenablog.com/entry/2020/09/03/%E9%A0%86%E5%BA%8F%E4%BB%98%E3%81%8D%E9%9B%86%E5%90%88%E3%82%82%E3%81%A9%E3%81%8D_Python_1

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