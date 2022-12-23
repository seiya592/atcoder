"""
2022/11/26 20:58:21
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


N,M = IIS()
A = LIIS()

#　素直に入れ替える　入れ替えるときに何の数字と何の数字を入れ替えたかをメモ
LR = []
B = []
for i in range(N):
    B.append(i+1)

for a in A:
    LR.append((B[a-1],B[a]))
    B[a-1], B[a] = B[a],B[a-1]

#各数字のインデックス
C = [0] * (N+1)
for i in range(N):
    C[B[i]] = i+1

for l,r in LR:
    if l != 1 and r != 1:
        print(C[1])
    else:
        if l == 1:
            print(C[r])
        else:
            print(C[l])

# #１から連続した数がどこまであるか
#
# # flg = [0] * N #初めてその数が出たフラグ
#
# LtoR = [0] * M  #左から見ていって１から連続した数
# now = 1
# for i in range(M):
#     if now == A[i]:
#         now+=1
#     LtoR[i] = now
# LtoR = [0] + LtoR
#
# RtoL = [0] * M
# #
# # for i in reversed(range(M)):
