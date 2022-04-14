# https://maspypy.com/atcoder-%e5%8f%82%e5%8a%a0%e6%84%9f%e6%83%b3-2020-06-27abc-172#toc4
def div_count(N):
    """
    1~Nまでの各値の約数の数をカウント
    O(NLogN)
    :return:List
    """
    div = [0] * (N+1)
    for n in range(1,N+1):
        for a in range(n, N+1, n):  #a = nからnステップ毎の値 →　div[a]約数にnが含まれている
            div[a] += 1
    return div
