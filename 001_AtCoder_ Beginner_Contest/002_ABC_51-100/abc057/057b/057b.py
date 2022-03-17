#18:38~
import sys

N,M = (map(int, input().split()))
humans = [list(map(int, input().split())) for i in range(N)]
cps = [list(map(int, input().split())) for i in range(M)]

minPoint = []
for human in humans:
    i = 1
    data = sys.maxsize
    for cp in cps:
        tmp = abs(human[0] - cp[0]) + abs(human[1] - cp[1])
        if data > tmp:
            data = tmp
            rtn = i
        i += 1

    minPoint.append(rtn)

for min in minPoint:
    print(min)