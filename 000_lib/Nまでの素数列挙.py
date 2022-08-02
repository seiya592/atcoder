def primes_dict(n):
    """
    10**7 は3000msなので無理
    2~Nまでの素数列挙
    :param n:
    :return:
    """
    #
    prime_list = []
    non_prime_list = []
    k_list = []
    number_dict = {
        i: None for i in reversed(range(n + 1))}
    #
    del number_dict[0]
    del number_dict[1]
    while True:
        # get prime
        prime, _ = number_dict.popitem()
        prime_list.append(prime)
        if prime * prime > n:
            break

        # get non primes
        non_prime_list.append(prime * prime)
        while True:
            k, _ = number_dict.popitem()
            k_list.append(k)
            if prime * k > n:
                break
            non_prime_list.append(prime * k)

        while k_list:
            number_dict[k_list.pop()] = None

        # delete non prime
        while non_prime_list:
            del number_dict[non_prime_list.pop()]

    while number_dict:
        prime, _ = number_dict.popitem()
        prime_list.append(prime)

    return prime_list

def primes_dict2(n):
    """
    O(N loglog N)   10**7は461ms  3*10**7で1366ms（現実的なのはここくらいまで？ 素数が1857859個なのでそのあとに線形で何かできたりはする）
    2~nまでの素数列挙
    :param n: 上限
    :return: list型 2~Nまでの素数リスト
    """
    arr = [0] * (n + 1)
    ret = []
    for i in range(2, n + 1):
        if arr[i]:
            continue
        ret.append(i)
        j = 1
        while i * j <= n:
            arr[i * j] += 1
            j += 1
    return ret
