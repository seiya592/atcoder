# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
N = int(input())
rtn = 0
if N >= 10 ** 3:
    rtn += (N - 10 ** 3) + 1
if N >= 10 ** 6:
    rtn += (N - 10 ** 6) + 1
if N >= 10 ** 9:
    rtn += (N - 10 ** 9) + 1
if N >= 10 ** 12:
    rtn += (N - 10 ** 12) + 1
if N >= 10 ** 15:
    rtn += (N - 10 ** 15) + 1
print(rtn)