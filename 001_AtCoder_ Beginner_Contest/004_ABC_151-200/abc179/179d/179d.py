def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

#解説AC

N, K  = IIS()
LR = LLIIS(K)

dp = [0] * (N+1)
dp[1] = 1

dpsum = [0] * (N+1)
dpsum[1] = 1

#貰う
for n in range(2,N+1):
    for l,r in LR:
        if n-l < 0:     # 貰う要素区間の一番右が負数だと無駄な為避ける
            continue
        # L-R間のdpの結果を貰う
        # 連続した部分の結果を貰うので累積和で求めることができる　（連続したという制約がないと累積和は使えなさそう）
        # 貰うDPで1つ前の値は計算済みなので、累積和を更新しながらある区間l-rが影響している[n-r]-[n-l]区間のdpの累積和を貰ってくる
        dp[n] += dpsum[n-l] - dpsum[max(n-r-1,0)] #L-R間の途中から更新されている可能性がある為Rは0以上にする
        dp[n] %= 998244353
    dpsum[n] = (dp[n] + dpsum[n-1])%998244353
print(dp[N])