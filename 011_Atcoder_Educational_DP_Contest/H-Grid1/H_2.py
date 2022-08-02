import collections


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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


H,W = IIS()
A = LI(H)

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
Q = collections.deque()
Q.append((0,0))
# 配る

done = [[False] * W for _ in range(H)]

while Q:
    i,j = Q.popleft()
    if done[i][j]:
        continue
    done[i][j] = True
    if i+1 < H and A[i+1][j] == '.':
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= 10 ** 9 + 7
        Q.append((i+1,j))
    if j+1 < W and A[i][j+1] == '.':
        dp[i][j+1] += dp[i][j]
        dp[i][j+1] %= 10 ** 9 + 7
        Q.append((i,j+1))

print(dp[-1][-1])