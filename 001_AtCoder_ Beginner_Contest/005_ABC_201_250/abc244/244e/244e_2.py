def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

N, M, K, S, T, X = IIS()
E = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = IIS()
    E[u].append(v)
    E[v].append(u)

dp = [[[0] * 2 for _ in range(N + 1)] for _ in range(K + 1)]
# dp[K回移動した後][現在位置の頂点][Xが奇数か偶数か ０=偶数]

# スタート地点は1通り
dp[0][S][0] = 1

for k in range(1, K + 1):
    for i in range(1, N + 1):
        for x in range(2):

            tmp = 0
            for e in E[i]:
                tmp += dp[k - 1][e][x]  # 1つ前の移動時につながっている辺の通りすべてを足す

            tmp = tmp % 998244353
            # 奇数か偶数反転確認
            if i == X:
                dp[k][i][x - 1] = tmp  # xをマイナスで反転動作と同等
            else:
                dp[k][i][x] = tmp

print(dp[K][T][0])