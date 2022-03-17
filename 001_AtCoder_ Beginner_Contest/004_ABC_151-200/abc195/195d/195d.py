# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import copy
import heapq

N,M,Q = (map(int, input().split()))
WV = [list(map(int, input().split())) for i in range(N)]
X = list(map(int, input().split()))
Query = [list(map(int, input().split())) for i in range(Q)]

WV.sort(key=lambda x:x[1],reverse=True)
rtn = []
for Q in Query:
    XX = copy.copy(X)
    XX[Q[0]-1:Q[1]] = []
    XX = heapq.nlargest(min(N,len(XX)), XX)
    XX.sort()
    tmp = 0
    for wv in WV:
        for xx in XX:
            if wv[0] <= xx:
                tmp += wv[1]
                XX[XX.index(xx)] = 0
                break
    rtn.append(tmp)
for r in rtn:
    print(r)