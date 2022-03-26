def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
Nstr = str(N)
dp = [[[0] * 2 for _ in range(10)]for _ in range(len(Nstr)+1)]
#dp[桁][１の出現回数　上限9][未満フラグ]
dp[0][0][0] = 1


for i in range(len(Nstr)):
    for j in range(9):
        for k in range(2):
            loop = 9 if k else int(Nstr[i])
            for d in range(loop+1):
                if d == 1:
                    dp[i+1][j+1][k | (d < int(Nstr[i]))] += dp[i][j][k]
                else:
                    dp[i + 1][j][k | (d < int(Nstr[i]))] += dp[i][j][k]

ans = 0
for i in range(10):
    ans += i * (dp[len(Nstr)][i][0] + dp[len(Nstr)][i][1])
print(ans)