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

# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_E

X = I()
Y = I()

dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]

for i in range(len(X)+1):
    dp[i][0] = i
for j in range(len(Y)+1):
    dp[0][j] = j

for i in range(1,len(X)+1):
    for j in range(1,len(Y)+1):


        a = dp[i-1][j] + 1  #追加
        b = dp[i][j-1] + 1  #削除
        c = dp[i-1][j-1] + (0 if X[i-1] == Y[j-1] else 1)   # 置換
        dp[i][j] = min(a,b,c)

print(dp[-1][-1])
