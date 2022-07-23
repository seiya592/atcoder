# https://note.nkmk.me/python-gcd-lcm/
from functools import reduce
import math
def my_gcd(numbers):
    """
        O(?)
        リスト内のすべての要素の最小公倍数を求める
        :param numbers:
        :return:numbersの要素の中の最小公倍数
        """

    return reduce(math.gcd, numbers)