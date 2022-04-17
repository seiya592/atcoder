import queue


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
from collections import deque

H,W = IIS()
C = LLIIS(H)

dp = [[0]*W for _ in range(H)]
done = [[False]*W for _ in range(H)]
dp[0][0] = 1
Q = deque()
Q.append([0,0])

while len(Q) > 0:
    x,y = Q.popleft()
    if done[x][y]:
        continue
    done[x][y] = True

    for t1, t2 in [[1,0],[0,1]]:
        if t1+x<H and t2+y<W :
            if C[t1+x][t2+y] == '.':
                dp[t1+x][t2+y] = max(dp[t1+x][t2+y], dp[x][y]+1)
                Q.append([t1+x,t2+y])

ans = 0
for d in dp:
    ans = max(max(d),ans)
print(ans)
