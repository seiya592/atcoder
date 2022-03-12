N,X = map(int,input().split())
al = 0
rtn = -1
flg = True
for i in range(N):
    V,P = map(int, input().split())
    al += V * P
    if flg == True and al > X * 100:
        rtn = i + 1
        flg = False

print(rtn)