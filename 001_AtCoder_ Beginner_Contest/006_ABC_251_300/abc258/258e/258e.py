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
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

#解説AC

N, Q, X = IIS()
W = LIIS()

# 1週あたりの重さ
Ws = sum(W)

# 1周に X // Ws　掛かる　周回が終わった後同じ位置から　X % Ws分箱詰めをする
cycle = X // Ws         # ここ忘れてた
x = X % Ws

# Wを2週分持つ
Wt = W + W

next = []
cnt = [-1] * N
M = 0
while 2 ** M <= 10**12:
    next.append([-1]*N)
    M += 1


#尺取り法
l = 0
r = 0
s = 0

while l < N:
    while s < x:
        s += Wt[r]
        r += 1

    next[0][l] = r % N
    cnt[l] = r - l
    cnt[l] += cycle * N
    s -= Wt[l]
    l += 1

#ダブリング
for m in range(1,M):
    for n in range(N):
        next[m][n] = next[m-1][next[m-1][n]]


#query
for _ in range(Q):
    q = II()
    q -= 1
    now = 0
    for m in range(M):
        if has_bit(q,m):
            now = next[m][now]

    print(cnt[now])