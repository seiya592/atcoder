N, M = list(map(int, input().split()))
A = list(input() for _ in range(N))

# start = 0/ goal = 10
group = []
for i in range(11):
    group.append([])

for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            g = 0
        elif A[i][j] == 'G':
            g = 10
        else:
            g = int(A[i][j])
        group[g].append([i,j])

cost = []
INF = 100000000000000
for i in range(N):
    cost.append([INF] * M)

si, sj = group[0][0]
cost[si][sj] = 0

for n in range(1, 11):
    for i, j in group[n]:
        for i2, j2 in group[n-1]:
            cost[i][j] = min(cost[i][j], (abs(i-i2)+abs(j-j2)) + cost[i2][j2])
        if cost[i][j] == INF:
            print(-1)
            exit()

gi, gj = group[10][0]
print(cost[gi][gj])