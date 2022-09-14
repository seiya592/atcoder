"""
2022/08/30 17:21:23
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


M = II()

E = [[] for _ in range(10)]

for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

P = LIIS()
now = ['9'] * 10
for i,s in enumerate(P,start=1):
    now[s] = str(i)
S = ''.join(now[1:])
G = '123456789'
done = set()
done.add(S)

Q = collections.deque()
Q.append([S,0])

while Q:
    n, d = Q.popleft()
    if n == G:
        print(d)
        exit()

    t = list(n)
    # 9（空いている場所）を探す
    i = t.index('9')

    for e in E[i+1]:
        t = list(n)
        # 空いている場所と繋がっている辺
        #入れ替え
        t[e-1], t[i] = t[i], t[e-1]

        # 文字列に変換
        s = ''.join(t)
        if s in done:
            continue #すでに探索予定or探索終了ならならば何もしない

        Q.append((s,d+1))
        done.add(s)
print(-1)
