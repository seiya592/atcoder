# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import sys

N = int(input())
A = list(map(int, input().split()))
rtn = sys.maxsize
for i in range(1,2 ** N):
    tmp = 0
    tmprtn = 0
    judge = i & 1
    for j in range(N):
        if i >> j & 1 == judge:
            tmp |= A[j]
        else:
            tmprtn ^= tmp
            tmp = A[j]
            judge = i >> j & 1
    else:
        tmprtn ^= tmp
    rtn = min(rtn,tmprtn)
print(rtn)