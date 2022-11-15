"""
2022/10/22 20:58:18
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


N, X, Y = IIS()
A = LIIS()

#最初は絶対に右に行かないといけない　＝ 初めから右にずらしておく
START_X = A[0]
START_Y = 0

# XとY交互
ROW = []
COL = []
MAX_R = 0
MAX_C = 0
for i in range(1,N):
    if i % 2 == 0:
        COL.append(A[i])
        MAX_C += A[i]
    else:
        ROW.append(A[i])
        MAX_R += A[i]

def calc(L):
    # dpで考えられる組み合わせを計算
    ALL = len(L) * 10
    dp = [0] * (ALL + 1)
    dp[0] = 1

    for n in range(len(L)):
        for i in reversed(range(ALL+1)):
            if i+L[n] <= ALL and dp[i]:
                dp[i+L[n]] += dp[i]
    return dp

ROW_L = calc(ROW)
COL_L = calc(COL)

if (MAX_C + abs(X-START_X)) % 2:
    NO()
if (MAX_R + abs(Y-START_Y)) % 2:
    NO()

x = (MAX_C + abs(X-START_X)) // 2
y = (MAX_R + abs(Y-START_Y)) // 2

if 0<=x<= len(COL_L) and 0<=y<=len(ROW_L):
    if ROW_L[y] and COL_L[x]:
        YES()
print(NO())