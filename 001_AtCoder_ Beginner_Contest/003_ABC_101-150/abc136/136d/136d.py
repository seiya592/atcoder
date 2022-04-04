def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10000000)
import math

def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

S = I()
N = len(S)
MAX = int(math.log2(10**100))+1

dp = [[-1] * N for _ in range(MAX)]

for i in range(N):
    if S[i] == 'R':
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for n in range(1,MAX):
    for i in range(N):
        dp[n][i] = dp[n-1][dp[n-1][i]]

ans = [0] * N
for i in range(N):
    ans[dp[MAX-1][i]] += 1

for a in ans:
    print(a, end=' ')
print()