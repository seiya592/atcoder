def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

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

N = II()
P = primes_dict(10**6+1)

ans = 0
for i, q in enumerate(P[1:],start=1):
    tt = q**3
    if tt*2 > N:
        break
    ok = 0
    ng = i
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if P[mid] * tt <= N:
            ok = mid
        else:
            ng = mid
    if ok == ng:
        pass
    ans += ok+1

print(ans)