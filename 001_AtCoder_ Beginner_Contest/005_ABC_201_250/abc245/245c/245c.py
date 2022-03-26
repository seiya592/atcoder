def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, K = IIS()
A = LIIS()
B = LIIS()
tmp = []
tmp2 = []
tmp.append(A[0])
tmp.append(B[0])
for a, b in zip(A[1:],B[1:]):
    tmp2 = []
    flg = True
    aflg = True
    bflg = True
    for t in tmp:
        if aflg and abs(a - t) <= K:
            tmp2.append(a)
            flg = False
            aflg = False
        if bflg and abs(b - t) <= K:
            tmp2.append(b)
            flg = False
            bflg = False
    if flg:
        print('No')
        exit()
    tmp = tmp2
else:
    print('Yes')