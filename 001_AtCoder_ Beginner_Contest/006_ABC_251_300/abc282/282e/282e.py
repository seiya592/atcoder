"""
2022/12/17 22:12:12
"""
import heapq


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
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17
import math
def mod_pow(a,b,m):
    """
    Division で使用する関数
    a ** b mod m を求める
    組み込み関数 pow(a,b,m)より早い
    """
    ALL = math.ceil(math.log2(b)) + 1

    ans = 1
    t = a
    for i in range(ALL):
        if b & (1 << i):
            ans *= t
            ans %= m
        t *= t
        t %= m
    return ans

N,M = IIS()

A = LIIS()
E = [[0]*(N) for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        t = (mod_pow(A[i],A[j],M) + mod_pow(A[j],A[i],M))%M
        E[i][j] = t
        E[j][i] = t



Q = []
heapq.heapify(Q)

done = [0] * N
done[0] = 1

for i in range(N):
    heapq.heappush(Q,(-E[0][i],i))

cnt = 0
ans = 0
while Q and cnt < N:
    c,n = heapq.heappop(Q)
    if done[n]:
        continue

    ans += -c
    done[n] = 1
    cnt += 1
    for i in range(N):
        heapq.heappush(Q,(-E[n][i], i))

print(ans)


# cnt = 0
# done = [0] * N
# ans = 0
# while cnt < N:
#     Q = []
#     heapq.heapify(Q)
#     for i in range(N):
#         if done[i]:
#             continue
#         heapq.heappush(Q,(-max(E[i]), i))
#
#     t,j = heapq.heappop(Q)
#     done[j] = 1
#     ans += -t
#     cnt += 1
#     for i in range(N):
#         E[i][j] = 0
#
# print(ans)