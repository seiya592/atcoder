def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(lambda x: int(x) -1, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque
from collections import defaultdict

# 解説AC

N, M = IIS()
QL = [[] for _ in range(M)]
nokori = [0] * M
for i in range(M):
    nokori[i] = II()
    QL[i] = deque()
    QL[i].extend(LIIS()+[-1])

d = defaultdict(lambda: -1,{})  # d[色番号] = 筒番号
bingo = deque()     # ([一番上のボールが一致しの筒番号1, 一番上のボールが一致しの筒番号2])
pass

for i, q in enumerate(QL):
    j = q.popleft()
    if d[j] == -1:  #初めてなら
        d[j] = i
    else:           #2回目なら
        bingo.append([i, d[j]])

pass
for i in range(N):  # 全色分ループ

    if len(bingo) == 0:
        print('No')
        exit()

    nn = bingo.popleft()

    for n in nn:
        j = QL[n].popleft()
        if j != -1:
            if d[j] == -1:
                d[j] = n
            else:
                bingo.append([n,d[j]])


print('Yes')

