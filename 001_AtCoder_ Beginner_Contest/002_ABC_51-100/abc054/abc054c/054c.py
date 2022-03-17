#19:11~
import itertools

N,M = (map(int, input().split()))
graphs = [list(map(int, input().split())) for i in range(M)]

permList = list(itertools.permutations(range(1,N + 1)))
rtn = 0
for perm in permList:
    if perm[0] != 1:
        break
    flg2 = True
    for i in range(len(perm) - 1):
        flg = False
        for graph in graphs:
            if set(graph) == set([perm[i], perm[i + 1]]):
                flg = True
                break

        if flg == False:
            flg2 = False
            break

    if flg2 == True:
        rtn += 1

print(rtn)


