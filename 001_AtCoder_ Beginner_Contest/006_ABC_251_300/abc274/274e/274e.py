"""
2022/10/22 20:58:24
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**10
import math

# def has_bit(n, i) -> bool:
#     """
#     nで表現される集合に要素iが含まれているかを判定
#     :param int n: 集合
#     :param int i: 要素
#     :return:bool True→含まれている False→含まれていない
#     """
#     return (n & (1 << i)) > 0

# def calc(x,y,a,b):
#     return math.sqrt((x-a)**2 + (y-b)**2)

def takaracnt(n):
    ans = 0
    for i in range(1,M+1):
        if (n & (1 << i)) > 0:
            ans += 1
    return ans

N,M = IIS()
XY = LLIIS(N)
PQ = LLIIS(M)
XY = [[0,0]] + PQ + XY
ALL = 2 ** (N+M+1)

bit = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5]

dp = [[INF] * (ALL) for i in range(N+M+1)]
#dp[通った場所(一番右は原点、下M桁は宝箱)][最終地点]
dp[0][0] = 0

for n in range(ALL):
    takara = (2**takaracnt(n))
    # t = (n & (((2**(M)) - 1) << 1)) >> 1
    # takara = bit[t] + 1
    for i in range(N+M+1):  # 現在地
        x, y = XY[i]
        if not (n >> i) & 1 and n: continue

        for j in range(N+M+1):  # 行先
            if i != j and not (n & (1 << j)) > 0:
                a, b = XY[j]
                dp[j][n | (1 << j)] = min(dp[j][n | (1 << j)], dp[i][n] + (math.sqrt((x-a)**2 + (y-b)**2)/takara))
if M:
    ans = INF
    a = (ALL-1) ^ (((2**(M)) - 1) << 1)
    for i in range(2**M):
        tmp = a | (i<<1)
        ans = min(ans,dp[0][tmp])
    print(ans)
else:
    print(dp[0][-1])