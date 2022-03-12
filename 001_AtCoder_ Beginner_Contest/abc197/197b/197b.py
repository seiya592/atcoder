H,W,X,Y = (map(int, input().split()))

S = [list(input()) for i in range(H)]

#上側
rtn = 1
i=1
while True:
    if (X - 1) - i <= -1:
        break
    if S[(X-1) - i][Y-1] == '.':
       rtn +=1
    else:
        break
    i += 1


#下側
i=1
while True:
    if (X - 1) + i >= H:
        break
    if S[(X-1) + i][Y-1] == '.':
       rtn +=1
    else:
        break
    i += 1


#左側
i=1
while True:
    if (Y - 1) - i <= -1:
        break
    if S[X-1][(Y-1) - i] == '.':
       rtn +=1
    else:
        break
    i += 1


#右側
i=1
while True:
    if (Y- 1) + i >= W:
        break
    if S[X-1][(Y-1) + i] == '.':
       rtn +=1
    else:
        break
    i += 1


print(rtn)