
"""
1 ~ 2*10**5 までの値すべてに使用した場合、for文が59528480回  計算時間は833[ms]
"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def factorization_count(n):
    """
    O(N loglog N)   10**7は437ms  3*10**7で1293ms（現実的なのはここくらいまで？）
    2~nまでの素因数の 「種類」 をカウント
    :param n: 上限
    :return: list型 0~Nの素因数の種類数 (0,1は未定義（0）)
    """
    arr = [0] * (n + 1)
    for i in range(2, n + 1):
        if arr[i]:
            continue
        j = 1
        while i * j <= n:
            arr[i * j] += 1
            j += 1
    return arr