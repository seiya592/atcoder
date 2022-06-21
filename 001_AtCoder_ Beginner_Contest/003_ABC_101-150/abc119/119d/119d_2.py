def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0
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

N,A,B,C = IIS()
T = [A,B,C]
L = []
for _ in range(N):
    l = II()
    L.append(l)

def dfs(used_bit, x, cost):
    if x == 3:
        return cost

    ret = INF

    #A,B,Cに使う竹を決める
    for n in range(1,2**N):
        if used_bit & n:    #すでに使っているのが含まれている場合
            continue

        length = 0
        c = 0
        for i in range(n):
            if has_bit(n,i):
                if has_bit(n, i):
                    length += L[i]

        #合成のコスト計算
        c = (popcount(n)-1) * 10

        # 長さを調整
        if T[x] < length:
            c += (length - T[x])
        elif T[x] > length:
            c += (T[x] - length)

        ret = min(dfs(used_bit|n, x+1, c+cost), ret)

    return ret




print(dfs(0,0,0))

