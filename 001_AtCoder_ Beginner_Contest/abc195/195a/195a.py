# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

M,H = (map(int, input().split()))

if H % M == 0:
    print('Yes')
else:
    print('No')