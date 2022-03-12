# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

a,b = (map(int, input().split()))
c,d = (map(int, input().split()))

rtn = max(a-c,a-d,b-c,b-d)

print(rtn)

