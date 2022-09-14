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
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0


N = II()
E = [[] for _ in range(N)]

for n in range(N):
    A = II()
    for _ in range(A):
        x,y = IIS()
        E[n].append((x-1,y))

ALL = 2 ** N
ans = 0
for n in range(ALL):
    cnt = 0
    flg = True
    for i in range(N):
        if has_bit(n,i):
            cnt += 1
            for x,y in E[i]:
                if y != (n & (2 ** x) != 0):
                    flg = False
                    break
    if flg:
        ans = max(ans, cnt)
print(ans)