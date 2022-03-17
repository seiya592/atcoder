# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#21:54:00~
N,K = (map(int, input().split()))
p = list(map(int, input().split()))

p.sort()
rtn = 0
for p in p[:K]:
    rtn += p
print(rtn)