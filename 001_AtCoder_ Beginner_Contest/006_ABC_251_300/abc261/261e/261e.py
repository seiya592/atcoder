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
import sys
sys.setrecursionlimit(500000)
INF = 10**10
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

# 各ビットがどうなるかを考える
# none, and, or , xor
#もし0なら、もし１なら

N,C = IIS()

rank = [[0,1] for _ in range(30)]
#rank[n桁目][もし初期の値が0なら,もし初期の値が1なら]

for _ in range(N):
    t,a = IIS()
    if t == 1:
        # and
        for i in range(30):
            if has_bit(a,i):
                rank[i][0] &= 1
                rank[i][1] &= 1
            else:
                rank[i][0] = 0
                rank[i][1] = 0
    elif t == 2:
        for i in range(30):
            if has_bit(a, i):
                rank[i][0] = 1
                rank[i][1] = 1
            else:
                # rank[i][0]
                # rank[i][1]
                pass
    else:
        for i in range(30):
            if has_bit(a, i):
                rank[i][0] ^= 1
                rank[i][1] ^= 1
            else:
                rank[i][0] ^= 0
                rank[i][1] ^= 0

    ans = 0
    for i in range(30):
        if has_bit(C, i):
            ans += rank[i][1] << i
        else:
            ans += rank[i][0] << i
    print(ans)
    C = ans
