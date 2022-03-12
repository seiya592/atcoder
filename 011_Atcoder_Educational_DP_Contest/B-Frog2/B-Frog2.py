N, K = (map(int, input().split()))
h = list(map(int, input().split()))

total = [100000000000] * N

# 足場1 + Kまでの処理
total[0] = 0
for i in range(1,min(K+1, N)):
    tmp = 1000000000000
    for j in range(i):
        tmp = min(tmp, total[j] + abs(h[i] - h[j]))
    total[i] = tmp

for i in range(K+1, N):
    tmp = 1000000000000
    for j in range(i-K,i):
        tmp = min(tmp, total[j] + abs(h[i] - h[j]))
    total[i] = tmp
print(total[N-1])

