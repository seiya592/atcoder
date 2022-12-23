"""
2022/11/19 20:55:49
"""
import datetime


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


H,M = IS()
h = [0,0]
m = [0,0]

if len(H) == 2:
    h[0] = int(H[0])
    h[1] = int(H[1])
else:
    h[1] = int(H[0])

if len(M) == 2:
    m[0] = int(M[0])
    m[1] = int(M[1])
else:
    m[1] = int(M[0])
# h[0] = 0 if len(H) == 1 else int(H[0])
# h[1] = int(H[-1])
#
# m[0] = 0 if len(m) == 1 else int(M[0])
# m[1] = int(M[-1])


while True:
    t_h = h[0] * 10 + m[0]
    t_m = h[1] * 10 + m[1]

    if t_h <= 23 and t_m <= 59:
        print(h[0]*10+h[1],m[0]*10+m[1])
        exit()

    # if m[1] < 9:
    #     m[1] += 1
    # else:
    #     m[0] += 1
    #     m[1] = 0

    m[1] += 1

    if m[1] == 10:
        m[1] = 0
        m[0] += 1

    if m[0] == 6:
        m[0] = 0
        h[1] += 1

    if h[1] == 10:
        h[0] += 1
        h[1] = 0

    if h[0] == 2 and h[1] == 4:
        h[0] = 0
        h[1] = 0


# # now = datetime.time(hours=H,minute=M)
# now = datetime.time(hour=H,minute=M)
# while True:
#     pass
#     now = now + datetime.time(minute=1)
#
#     h = str(now.hour())
#     m = str(now.minute())
#
#     pass