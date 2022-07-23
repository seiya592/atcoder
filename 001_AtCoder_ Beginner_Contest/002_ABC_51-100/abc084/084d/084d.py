def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
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


prime_list = [False] * (10 ** 5 + 1)

for i in range(2,10 ** 5 + 1):
    prime_list[i] = isprime(i)

like = [0] * (10**5 + 1)

for i in range(3,10 ** 5 + 1):
    if prime_list[i] and prime_list[(i+1)//2]:
        like[i] = like[i-1] + 1
    else:
        like[i] = like[i-1]

Q = II()
query = [LIIS() for _ in range(Q)]
for l, r in query:
    print(like[r] - like[l-1])
