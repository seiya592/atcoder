# N = int(input())
# ten = [list(map(int,input().split())) for i in range(N)]
# listS = set(input() for i in range(N))
# A, B ,K = map(int, input().split())

def popcount(x):
    # https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


N, M = map(int, input().split())  # スイッチ種類/電球数
swList = [tuple(map(int, input().split())) for i in range(M)]
sw2List = []
sw3List = []
cmpList = tuple(map(int, input().split()))

for sw in swList:
    tmp = 0
    # 電球が持っているスイッチ番号を二進数にして別リストに格納
    for i in sw[1:]:  # 最初の要素は電球が持っているスイッチの個数なので無視する
        tmp += + (2 ** (i - 1))  # スイッチ番号をビット管理
    sw2List.append(tmp)

rtn = 0
for i in range(2 ** N):  # スイッチ種類の全組み合わせループ
    count = 0
    for sw in sw2List:  # 各電球ごと
        tmp = sw & i  # 今のスイッチの組み合わせ抽出
        if popcount(tmp) % 2 == cmpList[count]:  # 立っているビットをカウントし、あまりをコンペア
            count += 1  # 一致なら電球が点灯　＝　カウント
        else:
            break  # 不一致なら電球ループ抜ける

    if count == M:  # 全部の電球が点灯してたらoutput+1
        rtn += 1

print(rtn)

# 30m
