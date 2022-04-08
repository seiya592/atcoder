def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
import math

class RangeGcdQuery():
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
            self.seg[index] = math.gcd(self.seg[index * 2], self.seg[index * 2 + 1])


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

    def get_gcd(self):
        return self.seg[1]

N = II()
A = LIIS()
RGQ = RangeGcdQuery(N,A[-1])
for i, a in enumerate(A):
    RGQ.update(i, a)

ans = RGQ.get_gcd()

for i in range(N):
    if i % 2 == 0:
        RGQ.update(i+1,A[i])
        ans = max(ans,RGQ.get_gcd())
        # if i == N-1:
        #     RGQ.update(i - 1, A[i-1])
        #     RGQ.update(i, A[i-1])
        #     ans = max(ans, RGQ.get_gcd())
    else:
        RGQ.update(i-1,A[i])
        RGQ.update(i,A[i])
        ans = max(ans, RGQ.get_gcd())
        RGQ.update(i-1,A[i-1])



RGQ = RangeGcdQuery(N, A[-2])
for i, a in enumerate(A):
    RGQ.update(i, a)
ans1 = RGQ.get_gcd()
for i in range(N):
    if i % 2 == 0:
        RGQ.update(i+1,A[i])
        ans1 = max(ans1,RGQ.get_gcd())
        if i == N-1:
            RGQ.update(i + 1, A[i-1])
            RGQ.update(i, A[i-1])
            ans1 = max(ans1, RGQ.get_gcd())
    else:
        RGQ.update(i-1,A[i])
        RGQ.update(i,A[i])
        ans1 = max(ans1, RGQ.get_gcd())
        RGQ.update(i - 1, A[i - 1])

print(max(ans,ans1))