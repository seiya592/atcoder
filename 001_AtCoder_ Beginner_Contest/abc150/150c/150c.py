#21:54~

import itertools
import math
N = int(input())
subList = [list(map(int, input().split())) for i in range(2)]

# print(subList)

permList = list(itertools.permutations(range(1,N + 1)))
permLen = len(permList)
# print(permList)
# print(permLen)

retList = []
for sub in subList:
    for i in range(math.factorial(N - 1) * (sub[0] - 1),math.factorial(N - 1) * (sub[0])):
        if sub == list(permList[i]):
            retList.append(i + 1)
            break

# print(retList)
print(abs(retList[0] - retList[1]))