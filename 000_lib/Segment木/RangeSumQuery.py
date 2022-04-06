# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=jp
class RangeSumQuery():
    """
    一点加算　区間和
    """

    def __init__(self, length, default):
        self.SEG_LEN = 2 ** length.bit_length()
        self.seg = [default] * (self.SEG_LEN * 2)

    def add(self,index,value):
        """
        seg木のindexの要素にvalueを追加する
        :param index: 要素番号
        :param value: 値
        """
        index += self.SEG_LEN
        self.seg[index] += value
        while True:
            index //= 2
            if index == 0:
                break
            self.seg[index] = self.seg[index * 2] + self.seg[index * 2 + 1]

    def get_sum(self, left, right):
        """
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
                ret += self.seg[left]
                left += 1
            if right % 2 == 1:
                ret += self.seg[right - 1]
                right -= 1
            left //= 2
            right //= 2
        return ret