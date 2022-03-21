def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
AB = [LIIS() for _ in range(N)]

dp = [[] for _ in range(N+1)]
dp[0].append(0)

for i in range(1,N+1):
    a, b = AB[i-1]
    tmp = []

    for d in dp[i-1]:
        tmp.extend([a+d,b+d])

    tmp = set(tmp)

    dp[i] = list(tmp)

if dp[N].count(M):
    print('Yes')
else:
    print('No')