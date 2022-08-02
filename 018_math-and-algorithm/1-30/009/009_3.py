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


#普通にdp

N, S = IIS()
A = LIIS()

dp = [0] * (max(A) + S)
dp[0] = 1
for a in A:
    for i in reversed(range(S)):
        dp[i+a] += dp[i]
print(YES() if dp[S] else NO())
