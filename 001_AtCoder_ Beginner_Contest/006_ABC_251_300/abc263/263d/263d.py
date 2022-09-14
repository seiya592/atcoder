"""
2022/08/06 20:52:06
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
import sys
sys.setrecursionlimit(500000)
INF = 10**15
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

N, L, R = IIS()
A = LIIS()

#累積和
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])

# Lの操作をした場合の増減地
LL = [0]
#軽減率を求める
for i in range(1, N+1):
    LL.append(-(S[i] - L * i))
LL.append(0)
# Rの操作をした場合の増減
RR = []
for i in range(N, -1, -1):
    RR.append(-(S[N] - S[i] - R * (N-i)))
RR.reverse()

Rs = OrderBIT(RR)
Ls = OrderBIT(LL)

for r in RR:
    Rs.insert_val(r)
Ls.insert_val(0)

ans = S[N]
for i in range(N+1):
    tmp = S[N] + Rs.find_kth_val(0) + Ls.find_kth_val(0)
    ans = min(ans,tmp)
    Rs.delete_val(RR[i])
    Ls.insert_val(LL[i+1])
print(ans)


# tmp = S[N]
# pos = 0
# for i in range(1,N+1):
#     if tmp > S[N] - S[i] + L * i:
#         tmp = S[N] - S[i] + L * i
#         pos = i
#
# tmp = S[N] - S[pos] + L * pos
# pos2 = 0
#
# for i in range(N, pos, -1):
#     if tmp > (S[N] - S[pos] + L * pos) - (S[N] - S[i]) + R * (N-i):
#         tmp = (S[N] - S[pos] + L * pos) - (S[N] - S[i]) + R * (N-i)
# print(tmp)