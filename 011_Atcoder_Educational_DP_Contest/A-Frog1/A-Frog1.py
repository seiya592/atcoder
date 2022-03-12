N = int(input())
h = list(map(int,input().split()))

total = [10000000] * N
total[0] = 0
total[1] = total[0] + abs(h[0] - h[1])
for i in range(2,N):
    total[i] = min(total[i - 2] + abs(h[i-2] - h[i]), total[i -1] + abs(h[i-1]-h[i]))

print(total[N-1])