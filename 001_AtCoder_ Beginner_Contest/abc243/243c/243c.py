def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

leftwork = {}
rightwork = {}


N = II()
XY = [LIIS() for _ in range(N)]
S = I()

for i in range(N):
    x,y = XY[i]
    y = str(y)
    if S[i] == 'R':
        if y in rightwork:
            rightwork[y] = min(x, rightwork[y])
        else:
            rightwork[y] = x
        if y in leftwork:
            if leftwork[y] > rightwork[y]:
                print('Yes')
                exit()

    if S[i] == 'L':
        if y in leftwork:
            leftwork[y] = max(x, leftwork[y])
        else:
            leftwork[y] = x
        if y in rightwork:
            if leftwork[y] > rightwork[y]:
                print('Yes')
                exit()
print('No')