def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)


N = II()
XYZ = LLIIS(N)
ALL = 1 << N
dp = [[10**10] * N for _ in range(ALL)]
dp[0][0] = 0

for n in range(ALL):
    for i in range(N):
        for j in range(N):
            # i to j
            if i == j or has_bit(n,j):
                continue
            calc = abs(XYZ[j][0]-XYZ[i][0]) + abs(XYZ[j][1]-XYZ[i][1]) + max(0,XYZ[j][2]-XYZ[i][2])
            dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i] + calc)
print(dp[ALL-1][0])
