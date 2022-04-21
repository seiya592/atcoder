def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()

ng = [False] * (300+1)
for _ in range(3):
    a = II()
    ng[a] = True

dp = [False] * (N+1)
dp[N] =  True if not ng[N] else False
i = N
for _ in range(100):
    for n in range(max(i-3,0),i):
        if not ng[n]:
            dp[n] = dp[i]
            i = n
            break
print('YES' if dp[0] else 'NO')