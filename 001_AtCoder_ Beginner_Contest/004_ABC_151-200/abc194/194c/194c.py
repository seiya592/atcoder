# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N = int(input())
A = list(map(int, input().split()))

rtn = 0
t = 0
for i in range(1,N):
    for j in range(0,i):
        t += 1
        # rtn += (A[i] - A[j]) ** 2
print(rtn)
print(t)