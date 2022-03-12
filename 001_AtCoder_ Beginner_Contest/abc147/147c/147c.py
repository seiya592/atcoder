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

N = int(input())
syougen_lst = []
for _ in range(N):
    A = int(input())
    tmp = [list(map(int, input().split())) for i in range(A)]
    syougen_lst.append(tmp)

rtn = 0
for i in range(1, 2 ** N):  #真と偽決め打ち　ビットで判定　1：真　0：偽
    flg = True
    for j in range(1,N + 1):    #真決め打ちの人数分ループする
        if i & (1 << (j - 1)) == 0:   #偽の話は聞かなくていいので飛ばす
            continue
        if flg == False:
            break
        for lst in syougen_lst[j - 1]: #真決め打ってる人の証言を持ってくる
            if not(((i >> (lst[0] - 1)) & 1) == lst[1]):    #証言が矛盾していないかチェック
                flg = False

    #真決め打ちの人の証言に矛盾がなければrtn更新
    if flg == True:
        rtn = max(rtn,popcount(i))

print(rtn)
# N = int(input())
#
# def makeJudgeList(inLst):
#     Tbit = 0
#     Fbit = 0
#     for lst in inLst:
#         if lst[1] == 1:
#             Tbit += (1 << (lst[0] - 1))
#         elif lst[1] == 0:
#             Fbit += (1 << (lst[0] - 1))
#     return Tbit, Fbit
#
# def popcount(x):
#     # https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
#     '''xの立っているビット数をカウントする関数
#     (xは64bit整数)'''
#
#     # 2bitごとの組に分け、立っているビット数を2bitで表現する
#     x = x - ((x >> 1) & 0x5555555555555555)
#
#     # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
#     x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
#
#     x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
#     x = x + (x >> 8)  # 16bitごと
#     x = x + (x >> 16)  # 32bitごと
#     x = x + (x >> 32)  # 64bitごと = 全部の合計
#     return x & 0x0000007f
#
# syougen_lst = []
# for _ in range(N):
#     A = int(input())
#     tmp = [list(map(int, input().split())) for i in range(A)]
#     syougen_lst.append(tmp)
#
# # print(syougen_lst)
#
# syougen_lst2 = []
#
# for lst in syougen_lst:
#     T, F = makeJudgeList(lst)
#     syougen_lst2.append([T,F])
# # print(syougen_lst2)
#
# def checkBit(lst,Tbit,Fbit,check,syougen_lst2):
#     for lst2 in lst:
#         if lst2[1] == 1 and check[lst2[0] - 1] == 0:
#             check[lst2[0] - 1] = 1
#             Tbit += syougen_lst2[lst2[0] - 1][0]
#             Fbit += syougen_lst2[lst2[0] - 1][1]
#             Tbit,Fbit = checkBit(syougen_lst[lst2[0] - 1],Tbit,Fbit,check,syougen_lst2)
#     return Tbit,Fbit
#
#
# rtn = 0
# for i in range(N):
#     check = [0] * N
#     Tbit = syougen_lst2[i][0]
#     Fbit = syougen_lst2[i][1]
#
#     Tbit,Fbit = checkBit(syougen_lst[i],Tbit,Fbit,check,syougen_lst2)
#
#
#     if (Tbit & Fbit) == 0:
#         if Tbit == 0 and rtn == 0:
#             rtn = 1
#         elif rtn < popcount(Tbit):
#             rtn = popcount(Tbit)
#
# print(rtn)


