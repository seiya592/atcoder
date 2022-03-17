# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import math
N = int(input())
A = tuple(map(int, input().split()))

def a(n):
    return n % 200

AA = list(map(a,A))
AA.sort()
rtn = 0
for i in range(201):
    tmp = AA.count(i)
    if tmp >= 2:
        rtn += sum(range(1,tmp))
print(rtn)

