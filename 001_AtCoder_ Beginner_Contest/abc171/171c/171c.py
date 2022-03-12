# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#21:56:20~
N = int(input())
rtn = ''
while True:
    rtn = chr(ord('a') + ((N  - 1) % 26)) + rtn
    N = (N - 1) // 26
    if N <= 0:
        break
print(rtn)