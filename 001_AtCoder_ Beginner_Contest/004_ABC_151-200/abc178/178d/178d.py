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


N = II()

#dp[n] = 総和がnの数列数
dp = [0] * (N+1)
dp[0] = 1       # 空リスト0,1,2が同じなので代表で0を1にしておく
for n in range(3,N+1):
    for i in range(0,n-2):      # 現在より3つ下以上の値は3以上の数を１つ追加するだけで使いまわしが出来るので全部足す
        dp[n] += dp[i]
        dp[n] %= 10**9+7
print(dp[-1])