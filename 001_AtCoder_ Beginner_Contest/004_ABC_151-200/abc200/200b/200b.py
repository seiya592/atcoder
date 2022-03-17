# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N,K = (map(int, input().split()))
t = N
for i in range(K):
    if t % 200 == 0:
        t = t // 200
    else:
        t = int(str(t) + '200')

print(t)
