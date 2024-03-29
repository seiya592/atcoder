def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja#

N = II()
if N < 2:
    print(1)
    exit()

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])