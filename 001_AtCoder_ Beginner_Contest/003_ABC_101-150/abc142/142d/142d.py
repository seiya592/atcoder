def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def isprime(n: int) -> bool:

    # 1以下は素数ではないので排除
    if n <= 1:
        return False

    # 2からnの2分の1乗までのループ
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            # 割り切れる値があれば素数ではないのでFalseを返す
            return False
    # ここまでくれば素数
    return True

A, B = IIS()
a = set(make_divisors(A))
b = set(make_divisors(B))
C = a & b

ans = 0
for c in C:
    ans += 1 if c == 1 or isprime(c) else 0
print(ans)