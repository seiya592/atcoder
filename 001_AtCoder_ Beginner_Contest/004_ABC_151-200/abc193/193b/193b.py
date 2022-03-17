# a,b,c,d = (map(int, input().split()))

N = int(input())
sunukeList = [list(map(int, input().split())) for i in range(N)]
rtn = []
rtn.append(100000000000000000)
for lst in sunukeList:
    if lst[2] - lst[0] > 0:
        rtn.append(lst[1])
if min(rtn) == 100000000000000000:
    print(-1)
else:
    print(min(rtn))