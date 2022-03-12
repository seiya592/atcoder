#21:18:20~
N,Q = (map(int, input().split()))
S = input()
a = [0]
# lrList = [list(map(int, input().split())) for i in range(Q)]

# for lr in lrList:
rtn = 0
for i in range(1,N):
    if S[i - 1] == 'A' and S[i] == 'C':
        rtn += 1
    a.append(rtn)

for i in range(Q):
    l, r = (map(int, input().split()))
    print(a[r - 1] - a[l - 1])

# for i in range(Q):
#     l, r = (map(int, input().split()))
#     print(S.count('AC',l - 1,r))
