def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**10
def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

# https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f
N = II()
A = LLIIS(N)
M = II()
E = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = IIS()
    x -= 1
    y -= 1
    E[y].append(x)
    E[x].append(y)

ALL = 2 ** N

dp = [[INF] * N for _ in range(ALL)]
for i in range(N):
    dp[1<<i][i] = A[i][0]

for n in range(ALL):
    next = popcount(n)
    for i in range(N):  # 最後の走者
        if has_bit(n,i):
            for j in range(N): # 次の走者
                if not has_bit(n,j):
                    if not j in E[i]:
                        dp[n|1<<j][j] = min(dp[n|1<<j][j], dp[n][i] + A[j][next])
ans = min(dp[ALL-1])
print(ans if ans != INF else -1)