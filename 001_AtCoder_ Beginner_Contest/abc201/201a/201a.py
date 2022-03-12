# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
A,B,C = (map(int, input().split()))

if A - B == B - C or B - C == C - A or B - A == A - C:
    print('Yes')
else:
    print('No')