def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
E = [[] for _ in range(N)]



for _ in range(M):
    u, v = IIS()
    E[u-1].append(v-1)

flg = [0] * N   #0→未　１→操作中 ２→終了
ans = [0] * N

def dfs(n):
    flg[n] = 1
    for e in E[n]:
        if flg[e] == 1:
            flg[n] = 2
            ans[n] = 1
            return False
        elif flg[e] == 2:
            if ans[e] == 0:
                flg[n] = 2
                return True
            else:
                flg[n] = 2
                ans[n] = 1
                return False
        elif flg[e] == 0:
            if dfs(e) == False:
                flg[n] = 2
                ans[n] = 1
                return False
    flg[n] = 2
    return True



while True:
    if not 0 in flg:
        break
    else:
        dfs(flg.index(0))

print(sum(ans))