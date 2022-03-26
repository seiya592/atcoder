def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

A, B = IIS()

# AとBに使用するので関数化
def func(n):
    dp = [[[0] * 2 for _ in range(2)] for _ in range(64)]  # dp[i桁目(64桁まで対応）][未満フラグ][4,9が入っているフラグ]
    n_str = str(n)
    dp[0][0][0] = 1

    for i in range(len(n_str)):
        for j in range(2):
            for k in range(2):
                loop = 9 if j else int(n_str[i])
                for d in range(loop+1):
                    dp[i+1][j | (d < int(n_str[i]))][k | (d==4) | (d==9)] += dp[i][j][k]
    return dp[len(n_str)][0][1] + dp[len(n_str)][1][1]


# A以上B以下での総数→ Bの総数からA-1の総数を引いた値
print(func(B) - func(A-1))