#22:00~
import  math
import itertools
N = int(input())
gridList = [list(map(int, input().split())) for i in range(N)]
# print(gridList)

permList = list(itertools.permutations(range(N)))
# print(permList)

AveList = []
def calcDistance(List1,List2):
    return math.sqrt(((List1[0] - List2[0]) ** 2) + ((List1[1] - List2[1]) ** 2))

for perm in permList:
    tmp = []
    for i in range(len(perm) - 1):
        tmp.append(calcDistance(gridList[perm[i]],gridList[perm[i + 1]]))
    AveList.append(sum(tmp))

rtn = sum(AveList) / len(AveList)

print(rtn)

