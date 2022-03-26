def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, K = IIS()
A = LIIS()
B = LIIS()

dp = [[False] * 2 for _ in range(N)]
dp[0][0] = True
dp[0][1] = True

for i in range(1,N):
    for j in range(2):
        for k in range(2):
            if dp[i-1][k]:
                to = B[i-1] if k else A[i-1]
                t = B[i] if j else A[i]
                dp[i][j] = (abs(to - t) <= K) | dp[i][j]

ans = 'Yes' if True in dp[N-1] else 'No'
print(ans)