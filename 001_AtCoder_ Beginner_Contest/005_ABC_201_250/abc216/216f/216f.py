"""
2022/11/11 18:01:26
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
MOD = 998244353

N = II()
A = LIIS()
B = LIIS()
AB = []
for a,b in zip(A,B):
    AB.append([a,b])

# 答えが小さい順から見る
AB.sort(key=lambda x:(x[0]))
MAX = max(A)

dp = [0] * (MAX+1)
dp[0] = 1

ans = 0
for n in range(N):
    a,b = AB[n]

    for i in range(MAX,-1,-1):  # AのMAXがA[n]になる時の組み合わせdp
        if i - b >= 0:
            dp[i] += dp[i-b]
            dp[i] %= MOD
            if i <= a:
                ans += dp[i-b]
                ans %= MOD
        else:
            continue
print(ans)