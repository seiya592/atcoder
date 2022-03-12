# N = int(input())
# ten = [list(map(int,input().split())) for i in range(N)]
# listS = set(input() for i in range(N))
# A, B ,K = map(int, input().split())

N = int(input())
Case = [list(map(int,input().split())) for i in range(N)]
rtn = []

for lst in Case:
    if lst[0] * 2 <= lst[1]:
        tmp = (lst[1] - (lst[0] * 2)) + 1
        rtn.append((tmp * (tmp + 1)) // 2)
    else:
        rtn.append(0)


for rtn2 in rtn:
    print(rtn2)