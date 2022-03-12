#18:41:15~
N,L = (map(int, input().split()))
cmp = []
for i in range(N):
    cmp.append((i+1) + L - 1)

if 0 in cmp:
    print(sum(cmp))
elif sum(cmp) > 0:
    print(sum(cmp) - min(cmp))
elif sum(cmp) < 0:
    print(sum(cmp) - max(cmp))