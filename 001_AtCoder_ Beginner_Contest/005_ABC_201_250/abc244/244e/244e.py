def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N,M,K,S,T,X = IIS()
E = []

for _ in range(M):
    u, v = IIS()
    E.append((u, v))


dp= [[[0] * 2 for _ in range(N + 1)] for _ in range(K+1)]
# dp[K回移動した後][現在位置の頂点][Xが奇数か偶数か ０=偶数]

#スタート地点は1通り
dp[0][S][0] = 1

for k in range(1, K+1):
    for u, v in E:
        for x in range(2):
            # 奇数か偶数反転確認
            if v == X:
                dp[k][v][x-1] += dp[k-1][u][x] % 998244353
                # if dp[k][v][x-1] >= 998244353:
                #     dp[k][v][x - 1] -= 998244353

            else:
                dp[k][v][x] += dp[k - 1][u][x] % 998244353
                # if dp[k][v][x] >= 998244353:
                #     dp[k][v][x] -= 998244353

            if u == X:
                dp[k][u][x - 1] += dp[k - 1][v][x] % 998244353
                # if dp[k][u][x-1] >= 998244353:
                #     dp[k][u][x-1] -= 998244353
            else:
                dp[k][u][x] += dp[k - 1][v][x] % 998244353
                # if dp[k][u][x] >= 998244353:
                #     dp[k][u][x] -= 998244353

print(dp[K][T][0] % 998244353)


# for _ in range(M):
#     u, v = IIS()
#     E[u].append(v)
#     E[v].append(u)

# def dfs(i):
#     global cnt
#     if cnt == (K+1):
#         if A.count(X) % 2 == 0 and A[K] == T:
#             global ans
#             ans += 1
#     else:
#         for e in E[i]:
#             A[cnt] = e
#             cnt += 1
#             dfs(e)
#             cnt -=1
#             A[cnt] = 0
#
#
# ans = 0
# A = [0] * (K+1)
# A[0] = S
# cnt = 1
# dfs(S)
# print(ans)
