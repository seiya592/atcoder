def Arithmetic_progression(a,d,n):
    """
    等差数列の和を求める

    l = [1,5,9,13,17]
    a = 1 l[0]
    d = 4 l[n+1] - l[n]
    n = 5 len(l)
    return = 45

    :param a:初項
    :param d:公差
    :param n:項数
    :return:等差数列の和
    """
    # return n * (a+(n*d)) // 2
    return n * (2*a+((n-1)*d)) // 2

print(Arithmetic_progression(1,1,4))