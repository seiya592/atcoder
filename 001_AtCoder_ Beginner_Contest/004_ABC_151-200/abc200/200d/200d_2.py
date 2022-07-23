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


N = II()
At = LIIS()
A = []
if N == 1:
    print('No')
    exit()

for a in At:
    A.append(a%200)

dp = [[0]*(201) for _ in range(N+1)]

dp[0][0] = 1
for n in range(N):
    for i in range(201):
        dp[n+1][i] += dp[n][i]
        dp[n+1][(200+i+A[n])%200] += dp[n][i]

#2以上の数を求める
target = -1
for i in range(201):
    if i == 0:
        if dp[N][0] >= 3:
            target = i
        continue

    if dp[N][i] >= 2:
        target = i

if target == -1:
    print('No')
    exit()

#極力同じ物をとらない方針
tmp = [False] * (N+1)
B = []
C = []
cnt = 0
def dfs(n,t):
    global cnt
    if n == -1:
        if not any(tmp):
            return

        cnt += 1
        if cnt == 1:
            for i in range(N+1):
                if tmp[i]:
                    B.append(i)
        else:
            for i in range(N+1):
                if tmp[i]:
                    C.append(i)
        return

    c = dp[n][t]
    #使わない
    if dp[n-1][t] and cnt < 2:
        dfs(n-1,t)
        c -= 1

    if c and cnt < 2:
        if dp[n-1][(200+t-A[n-1])%200]:
            tmp[n] = True
            dfs(n-1,(200+t-A[n-1])%200)
            tmp[n] = False

dfs(N,target)

print('Yes')
print(f'{len(B)}', *B)
print(f'{len(C)}', *C)