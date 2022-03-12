N = int(input())
abc = [[0,0,0]]+[list(map(int, input().split())) for _ in range(N)]

luck = [[0,0,0]]
for i in range(N):
    luck.append([-1,-1,-1])

for i in range(1, N+1):
    a, b, c = abc[i]
    luck[i][0] = max(luck[i-1][1],luck[i-1][2]) + a
    luck[i][1] = max(luck[i - 1][0], luck[i - 1][2]) + b
    luck[i][2] = max(luck[i - 1][1], luck[i - 1][0]) + c

print(max(luck[N]))



