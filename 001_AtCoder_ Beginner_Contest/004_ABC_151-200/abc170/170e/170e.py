def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10
import bisect

# 解説AC

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

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
class RangeMinimumQuery():
    """
    一点更新　区間取得
    """

    def __init__(self, length, default=0):
        self.SEG_LEN = 2 ** length.bit_length()
        self.seg = [default] * (self.SEG_LEN * 2)
        self.default = default

    def update(self,index,value):
        """
        一点更新
        seg木のindexの要素をvalueに更新
        :param index: 要素番号
        :param value: 値
        """
        index += self.SEG_LEN
        self.seg[index] = value
        while True:
            index //= 2
            if index == 0:
                break
            self.seg[index] = min(self.seg[index * 2], self.seg[index * 2 + 1])


    def get_min(self, left, right):
        """
        区間取得
        seg木の[left:right)の要素の最小値
        :param left: 左側（含まれる）
        :param right: 右側（含まれない）
        :return: 最小値
        """
        left += self.SEG_LEN
        right += self.SEG_LEN
        ret = self.default
        while left < right:
            if left % 2 == 1:
                ret = min(ret, self.seg[left])
                left += 1
            if right % 2 == 1:
                ret = min(ret, self.seg[right - 1])
                right -= 1
            left //= 2
            right //= 2

        return ret




N, Q = IIS()
AB = LLIIS(N)
CD = LLIIS(Q)

#multisetがとりうる値を求める
T = [[0] for _ in range(2*10**5+1)]
for a,b in AB:
    T[b].append(a)

for c, d in CD:
    T[d].append(AB[c-1][0])

#multiset生成
S = [OrderBIT(t) for t in T]

#multisetに代入、園児の幼稚園管理
Y = [-1] * (N+1)
for i, (a,b) in enumerate(AB):
    S[b].insert_val(a)
    Y[i+1] = b

#幼稚園のレート最大値を記録
RMQ = RangeMinimumQuery(2*10**5+1, INF)
for i, s in enumerate(S[1:],start=1):
    v = s.find_kth_val(s.count_lower(INF)-1)
    RMQ.update(i, v if v else INF)

#query処理
for c, d in CD:
    # 現在の園児の幼稚園
    y = Y[c]

    # 園児のレートを削除
    S[y].delete_val(AB[c-1][0])

    # 削除した後に更新
    v = S[y].find_kth_val(S[y].count_lower(INF) - 1)
    RMQ.update(y, v if v else INF)

    #転園
    Y[c] = d
    S[d].insert_val(AB[c-1][0])
    v = S[d].find_kth_val(S[d].count_lower(INF) - 1)
    RMQ.update(d, v if v else INF)
    print(RMQ.get_min(0,2*10**5+1))