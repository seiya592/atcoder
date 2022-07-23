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


class RangeSumQuery():
    """
    一点更新　区間取得
    """

    def __init__(self, length, default=0):
        self.SEG_LEN = 2 ** length.bit_length()
        self.seg = [default] * (self.SEG_LEN * 2)

    def add(self,index,value):
        """
        一点加算
        seg木のindexの要素にvalueを追加する
        :param index: 要素番号
        :param value: 値
        """
        index += self.SEG_LEN
        self.seg[index] ^= value
        while True:
            index //= 2
            if index == 0:
                break
            self.seg[index] = self.seg[index * 2] ^ self.seg[index * 2 + 1]

    def get_sum(self, left, right):
        """
        区間和
        seg木の[left:right)の要素の合計を返す
        :param left: 左側（含まれる）
        :param right: 右側（含まれない）
        :return: 合計
        """
        left += self.SEG_LEN
        right += self.SEG_LEN
        ret = 0
        while left < right:
            if left % 2 == 1:
                ret ^= self.seg[left]
                left += 1
            if right % 2 == 1:
                ret ^= self.seg[right - 1]
                right -= 1
            left //= 2
            right //= 2
        return ret

N,Q = IIS()
RSQ = RangeSumQuery(N+1)

A = LIIS()

for i, a in enumerate(A, start=1):
    RSQ.add(i, a)

for q in range(Q):
    t,x,y = IIS()
    if t == 1:
        RSQ.add(x,y)
    else:
        print(RSQ.get_sum(x,y+1))