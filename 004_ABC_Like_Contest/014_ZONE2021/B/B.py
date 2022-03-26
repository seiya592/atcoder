# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N,D,H = (map(int, input().split()))
DH = [list(map(int, input().split())) for i in range(N)]
rtn = 0
for d,h in DH:
    #変化の割合
    a = (H - h) / (D - d)
    b = H - (D * a)
    rtn = max(rtn,b)

print(rtn)