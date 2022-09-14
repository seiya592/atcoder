"""
2022/08/13 20:53:57
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


S = list(I())

D = {'a':0,
     't':1,
     'c':2,
     'o':3,
     'd':4,
     'e':5,
     'r':6}

N = [0] * 7

for i,s in enumerate(S):
    N[i] = D[s]


def bubble_sort(nlist):
    # 配列の要素数num
    num = len(nlist)
    ans = 0
    for i in range(num):
        swap = False
        for j in range(num - 1, i, -1):
            # 後ろから順番に隣同士の要素を比較する
            if nlist[j - 1] > nlist[j]:
                nlist[j - 1], nlist[j] = nlist[j], nlist[j - 1]
                swap = True
                ans += 1

        # 交換が行われなければ終了
        if swap == False:
            break

    return ans


print(bubble_sort(N))

# T = 'atcoder'
# ans = 0
# for i, t in enumerate(T):
#     ans += max(S.index(t) - i, 0)
# print(ans)