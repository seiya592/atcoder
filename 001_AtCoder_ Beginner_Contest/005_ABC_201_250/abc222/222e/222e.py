"""
2022/09/01 18:19:17
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, M, K = IIS()
A = LIIS()
E = [[] for _ in range(N+1)]
for i in range(N-1):
    u,v = IIS()
    E[u].append((v,i))
    E[v].append((u,i))

# i番目の頂点を何回通ったか記録
cnt = [0] * (N-1)

def dfs(n, o, t):
    global f

    if n == t:
        f = True
        return

    for e,i in E[n]:
        if o == e:
            continue
        if f:
            break

        cnt[i] += 1

        dfs(e,n,t)

        if not f:
            # 目的の頂点は見つからなかった
            cnt[i] -= 1

for m in range(1,M):
    f = False
    dfs(A[m-1], 0 ,A[m])


# ありえる数値の組み合わせ数をdpで列挙
cnt_sum = sum(cnt)
dp = [0] * (cnt_sum + 1)
dp[0] = 1
now = 0
cnt.sort()
for c in cnt:
    for i in range(now, -1, -1):
        dp[i+c] += (dp[i] % 998244353)
    now += c

if (cnt_sum + K) % 2 != 0 or cnt_sum < (cnt_sum + K) // 2:
    print(0)
elif (cnt_sum + K) // 2 < 0:
    print(0)
else:
    print(dp[(cnt_sum + K) // 2] % 998244353)
