def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


H,W = IIS()

A = [I() for _ in range(H)]

for i in reversed(range(H)):
    flg = True
    for j in range(W):
        if A[i][j] == '#':
            flg = False
            break
    if flg:
        A.pop(i)

for i in reversed(range(W)):
    flg = True
    for j in range(len(A)):
        if A[j][i] == '#':
            flg = False
            break
    if flg:
        for j in range(len(A)):
            A[j] = A[j][:i] + A[j][i+1:]

for a in A:
    print(a)
