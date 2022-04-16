# https://note.nkmk.me/python-gcd-lcm/
from functools import reduce
import math
def my_lcm(numbers):
    """
    O(N log (max(*numbers)))
    リスト内のすべての要素の最小公倍数を求める
    :param numbers:
    :return:numbersの要素の中の最小公倍数
    """

    def my_lcm_base(x, y):
        return (x * y) // math.gcd(x, y)
    return reduce(my_lcm_base, numbers, 1)

# print(my_lcm([5,10,100]))