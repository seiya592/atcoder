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
INF = 10**20


K = II()

# 各桁の和が９の倍数 = ９の倍数
# つまり各桁の和がKなのを見ればいい

if K % 9 != 0:
    print(0)
    exit()


dp = [0] * (K+1)
dp[0] = 1

#配る
# 現在桁の総和がnに桁を1つ足すと総和はn+1~n+9になる
for n in range(K):
    for k in range(n+1,min(n+10,K+1)):
        dp[k] += dp[n]
        dp[k] %= 10**9+7
print(dp[K])