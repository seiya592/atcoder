# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N,M = (map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rtn = list(set(A) ^ set(B))
rtn.sort
A = [str(a) for a in rtn]
A = ' '.join(A)
print(A)
