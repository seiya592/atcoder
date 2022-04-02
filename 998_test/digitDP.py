def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

N = 258742272267452
dp = [[0] * 2 for _ in range((len(str(N)) + 1))]
Nstr = str(N)
dp[0][0] = 1        #dp[i桁目まで][bool 0→0以上　Nstr[i]　までの数字で決める　1→0~9の数字で決める]

for i in range(len(str(N))):            # 現在見ている桁数
    for j in range(2):                  # N未満かどうか
        loop = 9 if j else int(Nstr[i])
        for k in range(loop + 1):
            dp[i+1][j | (k < int(Nstr[i]))] += dp[i][j]

pass


