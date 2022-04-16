def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#もらうDP
S = I()
T = I()
Sl = len(S)
Tl = len(T)
dp = [[0] * (Tl+1) for _ in range(Sl+1)]

for i in range(1,Sl+1):
    for j in range(1,Tl+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

#文字作り
i = Sl
j = Tl
ans = ''
while dp[i][j] != 0:
    if S[i-1] == T[j-1]:
        ans = S[i-1] + ans
        i -=1
        j -=1
    elif dp[i][j] == dp[i-1][j]:    # i-1 or j-1の値と現在の値は同じ
        i -= 1
    else:
        j -= 1
print(ans)
