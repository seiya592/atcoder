"""
2022/10/14 19:21:18
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


N = II()
H = LIIS()

dp = [INF] * N
dp[0] = 0
dp[1] = abs(H[0] - H[1])

for n in range(2,N):
    dp[n] = min(dp[n-1] + abs(H[n]-H[n-1]), dp[n-2] + abs(H[n]-H[n-2]))

now = N-1
ans = []
while now:
    ans.append(now+1)
    if dp[now-1] == dp[now] - abs(H[now] - H[now-1]):
        now -= 1
    else:
        now -= 2
else:
    ans.append(1)
print(len(ans))
print(*reversed(ans))