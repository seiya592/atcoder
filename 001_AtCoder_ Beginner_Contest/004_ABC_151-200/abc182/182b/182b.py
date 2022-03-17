#18:50:20~
N = int(input())
A = list(map(int, input().split()))

rtn = 0
rtn2 = 0
for i in range(2,max(A) + 1):
    tmp = 0
    tmp2 = 0
    for a in A:
        if a % i == 0:
            tmp += 1
            tmp2 = i
    if rtn < tmp:
        rtn = tmp
        rtn2 = tmp2

print(rtn2)