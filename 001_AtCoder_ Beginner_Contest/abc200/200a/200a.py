# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N = int(input())
a = N // 100
b = N % 100
rtn = 0
if b == 0:
    rtn = a
else:
    rtn = a + 1

print(rtn)

