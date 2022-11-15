"""
2022/10/14 17:41:47
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


R,C,K = IIS()
dp = [[0] * 4 for _ in range(C)]
# old = [[0] * 4 for _ in range(C)]
D = [[0]*C for _ in range(R)]
for _ in range(K):
    r,c,v = IIS()
    D[r-1][c-1] = v

#最初の行
dp[0][1] = D[0][0]
for c in range(C):
    for k in range(4):
        if c:
            dp[c][k] = max(dp[c][k], dp[c-1][k])
            if k:
                dp[c][k] = max(dp[c][k], dp[c-1][k-1] + D[0][c], dp[c][k - 1])
        elif k:
            dp[c][k] = max(dp[c][k], dp[c][k - 1])

old = [d[-1] for d in dp]

for r in range(1,R):
    for c in range(C):
        for k in range(4):
            if r:
                dp[c][k] = max(dp[c][k], old[c])
                if k == 1:
                    dp[c][k] = max(dp[c][k], old[c] + D[r][c])
            if c:
                dp[c][k] = max(dp[c][k], dp[c - 1][k])
                if k:
                    dp[c][k] = max(dp[c][k], dp[c - 1][k - 1] + D[r][c])
            if k:
                dp[c][k] = max(dp[c][k], dp[c][k - 1])
    old = [d[-1] for d in dp]

print(dp[-1][-1])