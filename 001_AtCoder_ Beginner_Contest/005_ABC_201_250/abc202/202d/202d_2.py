"""
2022/10/25 18:08:14
"""
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


A,B,K = IIS()

dp = [[0] * (B+1) for _ in range(A+1)]
dp[0][0] = 1

for i in range(A+1):
    for j in range(B+1):
        if i:
            dp[i][j] += dp[i-1][j]
        if j:
            dp[i][j] += dp[i][j-1]

def calc(a,b,k):
    if not a:
        return 'b' * b
    if not b:
        return 'a' * a

    if k <= dp[a-1][b]:
        return 'a' + calc(a-1,b,k)
    else:
        return 'b' + calc(a,b-1,k-dp[a-1][b])

print(calc(A,B,K))