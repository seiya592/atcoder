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
INF = 10**12


N, P, K = IIS()
A = LLIIS(N)

def calc(X, flg=True):
    dist = [[X if a == -1 else a for a in row] for row in A]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if dist[i][j] <= P:
                cnt += 1

    if not flg:
        if cnt >= K:
            return True
        return False
    else:
        if cnt <= K:
            return True
        return False

# P以下で到達できる組み合わせがK個以上存在する Xを探す
ok = INF
ng = 0
while abs(ok-ng) > 1:
    mid = (ok + ng) // 2

    if calc(mid):
        ok = mid
    else:
        ng = mid

# if ok == INF:
#     print(0)
#     exit()
# if ng == 0:
#     print('Infinity')
#     exit()


# P以下で到達できる組み合わせがK個以下存在する Xを探す
ok2 = 0
ng2 = INF

while abs(ok2-ng2) > 1:
    mid = (ok2 + ng2) // 2

    if calc(mid,False):
        ok2 = mid
    else:
        ng2 = mid


if ok2 < ok:
    print(0)
    exit()
if ng2 == INF:
    print('Infinity')
    exit()

print(ok2-ok+1)