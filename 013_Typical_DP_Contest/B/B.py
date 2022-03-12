# https://atcoder.jp/contests/tdpc/tasks/tdpc_game
A, B = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp = [[0] * (B + 1) for _ in range(A + 1)]

for i in range(A+1):
    for j in range(B+1):
        if i==0 and j == 0:
            tmp = 0
        elif i == 0:
            tmp = b[B + 1 - j] - dp[i][j-1]
        elif j == 0:
            tmp = a[A + 1 - i] - dp[i-1][j]
        else:
            tmp = max(a[A + 1 - i] - dp[i-1][j], b[B + 1 - j] - dp[i][j-1])
        dp[i][j] = tmp

print((sum(a)+sum(b)+dp[A][B]) // 2)