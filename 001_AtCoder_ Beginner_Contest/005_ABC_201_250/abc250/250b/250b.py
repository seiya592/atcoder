def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, A, B = IIS()

ans = [[''] * (N * B) for _ in range(N*A)]
def func(c):
    if c == '.':
        return '#'
    else:
        return '.'
mozi = '.'
for x in range(N):
    for y in range(N):
        for i in range(A):
            for j in range(B):
                ans[x*A+i][y*B+j] = mozi
        mozi = func(mozi)
    if N % 2 == 0:
        mozi = func(mozi)
for a in ans:
    print(''.join(a))