"""
2022/12/17 21:12:03
"""
import collections


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


N,M = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

if M == 0:
    print(N*(N-1)//2)
    exit()

C = [-1] * (N+1)    # 色

def calc(n):
    Q = collections.deque()
    Q.append((n, 0))
    B = 0
    W = 0
    Z = 0
    while Q:
        n,c = Q.popleft()
        if C[n] == c:
            continue
        if C[n] != -1:
            print(0)
            exit()
        C[n] = c
        if c == 0:
            B += 1
        else:
            W += 1
        for e in E[n]:
            Z+=1
            Q.append((e,1^c))

    return B,W,Z

cnt= 0
T = []
ans = 0
for i in range(1,N+1):
    if C[i] == -1:
        b,w,z = calc(i)
        ans += b * w - (z//2)
        ans += cnt * (b+w)
        cnt += (b+w)
print(ans)
# for i in range(1,N+1):
#     if C[i] == -1:
#         cnt += 1
#         T.append(calc(i))
# if cnt == 1:
#     print(C.count(1) * C.count(0) - M)
# elif cnt == 2:
#     print((T[0][0] + T[0][1]) * (T[1][0] + T[1][1]))
# else:
#     print(0)