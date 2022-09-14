"""
2022/08/08 16:10:05
"""
import bisect


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
INF = 10**10
class RangeAddQuery():
    """
    区間更新　一点取得
    """

    def __init__(self, length, default=0):
        self.SEG_LEN = 2 ** length.bit_length()
        self.seg = [default] * (self.SEG_LEN * 2)

    def get(self, index):
        """
        一点取得
        seg木のindexの要素にvalueを追加する
        :param index: 要素番号
        :param value: 値
        """
        index += self.SEG_LEN
        ret = self.seg[index]
        while True:
            index //= 2
            if index == 0:
                break
            ret += self.seg[index]
        return ret

    def add(self, left, right, value):
        """
        区間和
        seg木の[left:right)の要素の合計を返す
        :param left: 左側（含まれる）
        :param right: 右側（含まれない）
        :return: 合計
        """
        left += self.SEG_LEN
        right += self.SEG_LEN
        while left < right:
            if left % 2 == 1:
                self.seg[left] += value
                left += 1
            if right % 2 == 1:
                self.seg[right - 1] += value
                right -= 1
            left //= 2
            right //= 2

N, D, A = IIS()
XH = LLIIS(N)

XH.sort(key=lambda x:x[0])
X = [x for x,_ in XH]
RAQ = RangeAddQuery(N)

ans = 0
for i in range(N):
    x,h = XH[i]

    # 過去の爆弾を考慮した体力
    h -= A * RAQ.get(i)

    if h > 0:
        #体力を0にする為には爆弾いくつ？
        n = h // A
        n += 1 if h % A else 0

        ans += n

        #爆弾が届く範囲
        z = x + (D * 2)
        r = bisect.bisect_right(X,z)
        RAQ.add(i,r,n)
print(ans)