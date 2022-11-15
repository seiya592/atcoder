"""
2022/09/22 22:56:08
"""
import bisect


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


N,C = IIS()
XV = [[0,0]] + LLIIS(N)
X = [x for x,_ in XV]
def calc(XV):
    # 反時計回りで回った時の最大値を記録する
    R = {}
    now_sum = 0
    max_c = 0
    max_sum = 0
    for x,v in reversed(XV):
        now_sum += v
        if max_sum - max_c < now_sum - (C-x):
            max_sum = now_sum
            max_c = (C-x)
        R[x] = [max_sum, max_c]  # [最大値, 最大値になるように回る時のコスト]

    value = 0
    ans = 0
    for x,v in XV:
        value += v
        r = bisect.bisect_right(X,x)
        if r == len(X):
            r_sum = 0
            r_cost = 0
        else:
            r_sum, r_cost = R[X[r]]
        ans = max(ans,(value-x) + (r_sum-r_cost) - min(x,r_cost), value-x, r_sum-r_cost)

    return ans

print(calc(XV))