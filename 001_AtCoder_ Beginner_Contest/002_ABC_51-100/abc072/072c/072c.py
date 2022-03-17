# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

import collections

#20:50:35~
N = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
num = -1
rtn = 0
for i in range(0,10**5):
    tmp = c[i] + c[i + 1] + c[i + 2]

    if rtn < tmp:
        rtn = tmp

print(rtn)
