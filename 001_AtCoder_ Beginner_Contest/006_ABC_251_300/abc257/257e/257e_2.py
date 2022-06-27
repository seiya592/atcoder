def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10

#未AC

N = II()
C = LIIS()

dp = [''] * ((N+1)*2)

for n in range(N):
    for i in range(1,10):
        tmp = dp[n] + str(i)
        if len(dp[n+C[i-1]]) > len(tmp):
            continue
        if dp[n+C[i-1]] > tmp:
            continue
        dp[n+C[i-1]] = tmp
print(max(dp[:N+1]))