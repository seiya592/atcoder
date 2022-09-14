"""
2022/09/10 20:46:01
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
INF = 10**17


N = II()
S = LI(N)

D = collections.defaultdict(list)
for s in S:

    X_cnt = 0
    A_cnt = 0
    S_cnt = 0
    for c in reversed(s):
        #貢献度
        if '0'<=c<='9':
            A_cnt += int(c)

        if c == 'X':
            # 単体でのスコア
            S_cnt += A_cnt
            #Xの数
            X_cnt += 1

    D[X_cnt].append((A_cnt, S_cnt))

D = dict(D)
ans = 0
now = 0
for k in sorted(D.keys(),reverse=False):

    for x,s in sorted(D[k],key=lambda x:-x[0]):
        ans += now * k
        ans += s
        now += x
print(ans)
