N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for i in range(N)]
ws = [0]
vs = [0]
for w,v in wv:
    ws.append(w)
    vs.append(v)



#二次元配列作成
value = []
for i in range (N + 1):
    value.append([-10**17]* (W + 1))
value[0][0] = 0

for i in range(1, N + 1):   # 品物を１つずつ増やす
    for w in range(W + 1):  # wの重さまでの最大の価値
        value[i][w] = max(value[i][w], value[i-1][w])   # 品物を追加しない場合、1つ前の状態と変わらないので代入

        # 品物を追加する場合
        if w - ws[i] >= 0:  #　追加しても容量オーバーにならない場合
            value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

print(max(value[N]))

