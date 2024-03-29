def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
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

N,M = IIS()
A = LIIS()
B = LIIS()
C = LIIS()
D = LIIS()

CHOCO = []
BOX = []
for a,b in zip(A,B):
    CHOCO.append((a,b))

for c,d in zip(C,D):
    BOX.append((c,d))

CHOCO.sort(key=lambda x:-x[0])
BOX.sort(key=lambda x:-x[0])

T = OrderBIT(D)

i = 0 #チョコ
j = 0 #ボックス
while True:
    if i == N:
        print('Yes')
        exit()

    c_size = CHOCO[i][0]

    while j < M and c_size <= BOX[j][0]:
        T.insert_val(BOX[j][1])
        j+=1

    # 縦だけみてチョコが入る箱をTに貯めた。　そこから横の長さで一番効率のいい箱を見つける
    t = T.find_higher(CHOCO[i][1] -1)
    if t == -10**9:
        print('No')
        exit()

    T.delete_val(t)
    i += 1

