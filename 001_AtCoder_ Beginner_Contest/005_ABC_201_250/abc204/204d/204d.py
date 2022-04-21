import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
#　解説読み

N = II()
T = LIIS()
Ts = sum(T)
dp = [[False] * (Ts+1) for _ in range(N+1)]
# dp[n番目の料理までで][時間合計] = bool　n番目までの料理を組み合わせてt時間が作れるか？
dp[0][0] = True

if N == 1:
    print(T[0])
    exit()

#配るDP
for n in range(N):
    for t in range(Ts+1):
        if dp[n][t] and t+T[n] < Ts+1:
            dp[n+1][t+T[n]] = True      #n番目の料理を選択
            dp[n+1][t] = True           #n番目の料理を選択しない

# dp[N] →選べる組み合わせ　選ばなかった組み合わせがもう片方のオーブンの時間となる
# 組み合わせの中で半分より大きい最小値を選択
for n in range(math.ceil(Ts/2),Ts):
    if dp[N][n]:
        print(n)
        exit()