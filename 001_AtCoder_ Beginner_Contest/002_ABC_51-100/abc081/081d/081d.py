"""
2022/10/20 18:23:42
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
A = LIIS()

# 場合分けをする
MAX = max(A)
MIN = min(A)

if MAX > MIN >= 0:
    print(N-1)
    for i in range(1,N):
        print(i, i + 1)
elif 0 >= MAX > MIN:
    print(N-1)
    for i in range(N,1,-1):
        print(i,i-1)
else:
    if abs(MIN) > MAX:
        #minを探す
        for i in range(N):
            if MIN == A[i]:
                t = i+1
                break

        print(N*2-1)
        for i in range(1,N+1):
            print(t,i)
        for i in range(N, 1, -1):
            print(i, i - 1)

    else:
        for i in range(N):
            if MAX == A[i]:
                t = i + 1
                break
        print(N * 2 - 1)
        for i in range(1, N + 1):
            print(t, i)
        for i in range(1, N):
            print(i, i + 1)

# ans = []
#
# for i in range(1,N+1):
#     now = INF
#     under = A[i-1] if i != 1 else -INF
#     ans_x = 0
#     ans_y = 0
#     for j in range(0, N+1):
#         for k in range(0, N+1):
#             tmp = A[i] * 4 if i == j == k else A[i] + A[j] + A[k]
#
#             if now > tmp >= under:
#                 now = tmp
#                 ans_x = j
#                 ans_y = k
#     if ans_x:
#         ans.append((ans_x, i))
#     if ans_y:
#         ans.append((ans_y, i))
#     A[i] = now
#
# print(len(ans))
# for x,y in ans:
#     print(x,y)