def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


A = LIIS()

dp = [[0]*4 for _ in range(4)]

for i in range(4):
    dp[0][i] = A[i]

for i in range(1,4):
    for j in range(4):
        for k in range(max(0,j-1),min(4,j+2)):
            dp[i][j] += dp[i-1][k]
print(dp[3][3])