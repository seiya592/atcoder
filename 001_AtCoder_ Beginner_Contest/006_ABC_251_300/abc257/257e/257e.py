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
MOD = 10**20

#未AC

N = II()
C = LIIS()

# dp = [0] * ((N+1)*2)

# for n in range(N):
#     for i in range(1,10):
#         dp[n+C[i-1]] = max(dp[n] * 10 + i, dp[n+C[i-1]])
#
# print(max(dp[:N+1]))

dp = [[0] * 3 for _ in range((N+1)*2)]
#dp[支払額][MODで割った数]
for n in range(N):
    for i in range(1,10):
        tmp = (dp[n][0] * 10 + i) % MOD
        tmp2 = dp[n][1]*10 + ((dp[n][0] * 10 + i) // MOD)
        tmp3 = dp[n][2]*10 + (tmp2 % MOD)
        if tmp3 < dp[n+C[i-1]][2]:
            continue

        if tmp2 < dp[n+C[i-1]][1]:
            continue
        elif tmp2 > dp[n+C[i-1]][1]:
            dp[n+C[i-1]][0] = tmp
            dp[n + C[i - 1]][1] = tmp2
            dp[n + C[i - 1]][2] = tmp3

        else:
            if tmp > dp[n+C[i-1]][0]:
                dp[n + C[i - 1]][0] = tmp
                dp[n + C[i - 1]][1] = tmp2
                dp[n + C[i - 1]][2] = tmp3

ans = 0
ans2 = 0
ans3 = 0
for i in range(N+1):
    if ans3 > dp[i][2]:
        continue

    if ans2 < dp[i][1]:
        ans2 = dp[i][1]
        ans = dp[i][0]
    elif ans2 > dp[i][1]:
        continue
    else:
        if ans < dp[i][0]:
            ans = dp[i][0]
            ans2 = dp[i][1]
if ans3 == 0:
    if ans2 == 0:
        print(ans)
    else:
        print(str(ans2) + str(ans))
else:
    print(str(ans3) +str(ans2) + str(ans))
print()
# print(ans + ((ans2+(ans3*MOD))*MOD))