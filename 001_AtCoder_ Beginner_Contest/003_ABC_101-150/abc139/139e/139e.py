"""
2022/10/19 18:21:21
"""
import collections


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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
A = LLIIS(N)

Q = collections.deque()
# Q = [選手番号, 何回目の試合か]

play_cnt = [0] * N
# 選手iは何回試合したか

play_day = [0] * N
# 選手iは何日経過しているか

for i in range(N):
    Q.append((i,0))

while Q:
    n, c = Q.popleft()

    if c >= N - 1:
        #全試合完了している
        continue

    if play_cnt[n] > c:
        # 別の人視点で処理が終了している
        continue

    m = A[n][c] - 1     # 対戦相手
    if play_cnt[m] < N and A[m][play_cnt[m]] - 1 != n:
        # 対戦相手がまず別の相手と対戦しなくてはいけない
        continue

    day = max(play_day[n], play_day[m]) + 1         # 掛かる日数
    play_cnt[n] += 1
    play_cnt[m] += 1
    play_day[n] = day
    play_day[m] = day

    Q.append((n, c+1))
    Q.append((m, play_cnt[m]))


for c in play_cnt:
    if c != N-1:
        print(-1)
        exit()
ans = 0
for d in play_day:
    ans = max(ans, d)
print(ans)