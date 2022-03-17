# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Al = [0] * 100001
Bl = [0] * 100001
test = [0] * 10

for a in A:
    Al[a] += 1

for c in C:
    Bl[B[c- 1]] += 1
rtn = 0
for a,b in zip(Al,Bl):
    rtn += a*b

print(rtn)