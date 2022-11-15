"""
2022/10/01 20:39:11
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
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
A = LIIS()

A.sort()
Q = collections.deque()
QQ = collections.deque()
t = 0
for a in A:
    if t == a:
        QQ.append(a)
    else:
        t = a
        Q.append(a)

ans = 0
f = True
while Q or QQ:
    if Q:
        t = Q.popleft()
    else:
        f = False

    if f and ans + 1 == t:
        ans += 1
    else:
        if f:
            Q.appendleft(t)
        if len(QQ) >= 2:
            QQ.pop()
            QQ.pop()
            ans += 1
        elif len(QQ) == 1 and len(Q) >= 1:
            QQ.pop()
            Q.pop()
            ans += 1
        elif len(Q) >= 2:
            Q.pop()
            Q.pop()
            ans += 1
        else:
            break
print(ans)