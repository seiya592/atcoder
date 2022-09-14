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
A = LIIS()

#鳩ノ巣原理から8種類あれば256通りの組み合わせが作成でき、200通りの余りの種類ならば１つは必ず被る
N = min(N,8)
A = A[:8]

ALL = 2 ** N
ans = [0] * (200)

for n in range(ALL):
    t = 0
    l = []
    for i in range(N):
        if has_bit(n,i):
            t += A[i]
            l.append(i+1)

    t %= 200
    if ans[t]:
        B = l
        C = ans[t]
        print('Yes')
        print(len(B), *sorted(B))
        print(len(C), *sorted(C))
        exit()
    else:
        ans[t] = l
NO()