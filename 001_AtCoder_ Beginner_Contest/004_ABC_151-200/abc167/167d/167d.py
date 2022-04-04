def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)

def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)


#ダブリング

N, K = IIS()
A = LIIS()

dp = []
#dp[2**k][i番目の町からスタート]　= i番目の町から2**k移動した後の終点

M = 0
while 2**M < K:
    dp.append([-1] * (N+1))
    M += 1

for i, a in enumerate(A,start=1):
    dp[0][i] = a

for k in range(1,M):
    for i in range(1,N+1):
        dp[k][i] = dp[k-1][dp[k-1][i]]

ans = 1
for k in range(M):
    if has_bit(K,k):
        ans = dp[k][ans]

print(ans)