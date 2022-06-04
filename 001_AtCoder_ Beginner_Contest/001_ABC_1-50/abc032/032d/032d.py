import bisect


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


N, G = IIS()
V = []
W = []
for _ in range(N):
    v,w = IIS()
    V.append(v)
    W.append(w)

def func1():
    def has_bit(n, i):
        """
        nで表現される集合に要素iが含まれているかを判定
        :param n:int 集合
        :param i:int 要素
        :return:bool True→含まれている False→含まれていない
        """
        return (n & (1 << i) > 0)

    def calc(N,V,W):
        ret = []
        ALL = 2 ** N

        for n in range(ALL):
            v, w = 0, 0
            for i in range(N):
                if has_bit(n,i):
                    v += V[i]
                    w += W[i]
            ret.append([w,v])
        return ret

    def dp(WV):
        WV.sort(key=lambda x:(x[0],-x[1]))

        old_v = WV[0][1]
        ret = []
        ret.append([0,0])
        ret.append([WV[0][0], WV[0][1]])
        for w, v in WV[1:]:
            if v < old_v:
                ret.append([w,old_v])
            else:
                ret.append([w,v])
            old_v = max(v,old_v)
        return ret

    #半分全列挙
    V1, V2 = V[::2], V[1::2]
    W1, W2 = W[::2], W[1::2]
    N1, N2 = len(V1), len(V2)

    # 計算結果を入れる
    T1 = calc(N1,V1,W1)
    T2 = calc(N2,V2,W2)

    TT1 = dp(T1)
    TT2 = dp(T2)

    ans = 0
    t2 = [t[0] for t in TT2]
    for t1 in TT1:
        if t1[0] > G:
            continue
        n = bisect.bisect_right(t2,G-t1[0])
        # if n != 0:
        ans = max(ans, t1[1] + TT2[n-1][1])
        # else:
        #     ans = max(ans, t1[1])
    print(ans)

    # for t2 in TT2:
    #     if t2[0] > G:
    #         continue
    #     ans = max(ans, t2[1])

def func2():
    # 重さの最小値
    dp = [[INF] * (1000 * N + 1) for _ in range(N+1)]
    #dp[n番目の荷物][価値がv] = 最小の重さ
    dp[0][0] = 0
    #配る
    for n in range(N):
        for j in range(1000*N):
            dp[n+1][j] = min(dp[n+1][j], dp[n][j])
            if j + V[n] < (1000*N) + 1:
                dp[n+1][j+V[n]] = min(dp[n+1][j+V[n]], dp[n][j] + W[n])

    ans = 0
    for v,d in enumerate(dp[N]):
        if d <= G:
            ans = v
    print(ans)

def func3():
    # 価値の最大値
    dp = [[-1] * (1000 * N + 1) for _ in range(N+1)]
#     dp[n番目までの荷物][重さがw] = 価値の最大値
    dp[0][0] = 0
    # 配る
    for n in range(N):
        for j in range(1000*N):
            dp[n+1][j] = max(dp[n+1][j], dp[n][j])
            if j + W[n] < (1000*N)+1:
                dp[n+1][j+W[n]] = max(dp[n+1][j+W[n]], dp[n][j] + V[n])

    if G > 1000*N:
        ans = max(0,max(dp[N]))
        print(ans)
    else:
        ans = max(0,max(dp[N][:G+1]))
        print(ans)


# 半分全列挙 価値の最大値 重さの最小値 を求めるdp
if max(V) <= 1000:
    # 価値の最大値
    func2()
elif max(W) <=1000:
    # 重さの最小値
    func3()
else:
    # 半分全列挙
    func1()
