"""
2022/12/09 22:52:46
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


N, K = IIS()
E = [0] * (N+1)
dp = [[0] * 7 for _ in range(N+1)]

dp[0][0] = 1

for _ in range(K):
    a,b = IIS()
    E[a] = b

#もらうDP
for n in range(1,N+1):
    for i in range(1,4):
        for j in range(2):
            if E[n] != 0 and i != E[n]:
                continue
            for k in range(7):
                if i*2+j-1 == k:
                    continue
                if j == 0 and i*2 == k:
                    continue
                if j == 1 and i*2-1 != k:
                    continue
                dp[n][i*2+j-1] += dp[n-1][k] % 10000

print(sum(dp[N])%10000)
