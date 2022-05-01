def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
INF = 10**10

N,M = IIS()
AB = LLIIS(N)
dp = [[INF] * (M+1) for _ in range(N+1)]
dp[0][0] = 0
#dp[n番目までの部分和][総和] = n番目の値の使用個数
# もらうほうが書きやすいかも
for n in range(1,N+1):
    for i in range(M+1):
        # 選ばない場合
        dp[n][i] = 0 if dp[n-1][i] < INF else INF

        #選ぶ場合
        if i - AB[n-1][0] >= 0 and dp[n-1][i-AB[n-1][0]] < INF:     #要素外対策 and 選ぶ場合は1つ前の要素AがINF以外である必要がある(0の場合は1つ前以前の要素で何かしら達成できている)
            dp[n][i] = 1

        # 追加で選ぶ場合
        if i - AB[n-1][0] >= 0 and dp[n][i - AB[n-1][0]] < AB[n-1][1]:  #要素外対策 and 今回の要素nで-Aした値が存在する（!=INF）　かつ　まだB回使ってない場合
            dp[n][i] = dp[n][i - AB[n-1][0]] + 1

print('Yes' if dp[N][M] != 10**10 else 'No')