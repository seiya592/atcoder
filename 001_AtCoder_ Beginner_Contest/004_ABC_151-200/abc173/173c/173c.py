# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#21:09:10~
H,W,K = (map(int, input().split()))
gridList = [input() for i in range(H)]


def checkBlack(i,j):
    tmp = 0
    for h in range(H):
        if (i >> h) & 1 == 1:
            continue
        for w in range(W):
            if (j >> w) & 1 == 1:
                continue
            if gridList[h][w] == '#':
                tmp += 1
    if tmp == K:
        return 1
    else:
        return 0

rtn = 0
for i in range(2 ** H):
    for j in range(2 ** W):
        rtn += checkBlack(i,j)

print(rtn)