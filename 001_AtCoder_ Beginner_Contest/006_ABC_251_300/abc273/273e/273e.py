"""
2022/10/15 20:52:54
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


Q = II()

edge = [-1]
num = [-1]
adr = dict()
ptr = 0
max_ptr = 1
ans = []

for _ in range(Q):
    q = IS()
    if q[0] == 'DELETE':
        if ptr:
            ptr = edge[ptr]
    else:
        q,i = q
        if q == 'ADD':
            edge.append(ptr)
            num.append(i)
            ptr = len(edge) - 1
        elif q == 'SAVE':
            adr[i] = ptr
        elif q == 'LOAD':
            if i in adr:
                ptr = adr[i]
            else:
                ptr = 0

    ans.append(num[ptr])
print(*ans)