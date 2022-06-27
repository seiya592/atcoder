def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10

#解説AC

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

N,M,P,Q,R = IIS()
E = [[] for _ in range(N+1)]
for _ in range(R):
    x,y,z = IIS()
    E[x].append((y,z))  #女子Xが持っている男子Yに渡す幸福度Zのチョコ


ALL = 2**N
ans = 0
for n in range(ALL):
    if popcount(n) != P:
        # 女子の数があっていない場合
        continue
    tmp = [0] * M
    for i in range(N):
        if has_bit(n,i):
            for y,z in E[i+1]:
                # 今いる女子がある男子yにチョコを上げた場合の幸福度をカウント
                tmp[y-1] += z
    tmp.sort(reverse=True)
    #幸福度がより多く得られる男子上位Q名分を答えとしてカウント
    ans = max(ans, sum(tmp[:Q]))
print(ans)