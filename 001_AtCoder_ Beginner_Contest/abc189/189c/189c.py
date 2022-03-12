# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#22:31:35~
N = int(input())
A = list(map(int, input().split()))
rtn = 0
for i in range(len(A)):
    tmp = A[i]
    j = i - 1
    while j >= 0 and A[j] >= A[i]:
        tmp += A[i]
        j -= 1

    j = i + 1
    while j < len(A) and A[j] >= A[i]:
        tmp += A[i]
        j += 1

    rtn = max(rtn,tmp)

print(rtn)