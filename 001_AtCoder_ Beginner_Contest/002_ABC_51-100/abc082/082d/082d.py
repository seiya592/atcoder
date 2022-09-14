"""
2022/08/31 17:34:45　→ 17:55:00
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


S = I()
x,y = IIS()

# 最初のFはX+固定なので除外する
now = 0
while now < len(S) and S[now] == 'F':
    x -= 1
    now += 1

# X軸の移動要素とY軸の移動要素を抽出する
X = []
Y = []
f = 1   # 今現在のnow
s = 0
while True:
    if now < len(S) and S[now] == 'F':
        s += 1
    else:
        if f:
            # X軸
            if s:
                X.append(s)
        else:
            # Y軸
            if s:
                Y.append(s)
        f ^= 1
        s = 0
    now += 1

    if now > len(S):
        break

# 分解した後 X,Y軸それぞれで最終地点をx,yにできるかチェック
def calc(L, goal):
    # dpで振り分けれる組み合わせを作る
    ALL = sum(L)

    if not ALL:
        # 合計が0の場合は例外処理
        if goal != 0:
            NO()
        else:
            return

    dp = [0] * (8000*2+1)  #上限面倒なんで*2
    dp[0] = 1

    now = 0
    for n in L:
        for i in range(now,-1, -1):
            dp[i+n] += dp[i]
        now += n

    # 差分をgoalにする
    if (ALL+goal) % 2:
        #割り切れない場合は到達不可
        NO()
    t = (ALL + goal) // 2
    if not dp[t]:
        # 差分を作ることができないなら到達不可
        NO()

calc(X,x)
calc(Y,y)
YES()