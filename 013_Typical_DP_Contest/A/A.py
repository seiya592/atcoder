# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
N = int(input())
p2 = list(map(int, input().split()))
p = [0]
p = p + p2

P = sum(p)
exist = []
for i in range(N + 1):
    exist.append([False] * (P + 1))

exist[0][0] = True

for i in range(1, N + 1):
    for s in range(P + 1):
        if exist[i-1][s]:
            exist[i][s] = True
            continue
        if (s-p[i] >= 0) and exist[i-1][s-p[i]]:
            exist[i][s] = True

print(exist[N].count(True))