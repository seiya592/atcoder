N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for i in range(N)]
ws = [0]
vs = [0]
for w,v in wv:
    ws.append(w)
    vs.append(v)

# すべての価値の合計
V = sum(vs)



#二次元配列作成
weight = []
for i in range(N + 1):
    weight.append([10**17] * (V + 1))

weight[0][0] = 0

for i in range(1, N + 1):
    for v in range(V + 1):
        weight[i][v] = min(weight[i][v], weight[i-1][v])

        if v - vs[i] >= 0:
            weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]] + ws[i])

ans = 0
for i, w in enumerate(weight[N]):
    if w <= W:
        ans = max(ans, i)

print(ans)