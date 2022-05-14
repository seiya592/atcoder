def primes_dict(n):
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