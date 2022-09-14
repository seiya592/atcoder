"""
2022/08/21 20:49:46
"""
import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**15


class COMPRESS:
    """
    座標圧縮
    同じ値のデータは同じ順位で圧縮 n
    次に大きい値のデータ1つ前のデータの個数に関わらず n+1
    TODO:重複が存在する場合に次の順位を飛ばす/飛ばさない選べるように
    """

    def __init__(self, lst, rev=False):
        """
        O(NlogN)
        :param lst : list 圧縮するリスト
        :param rev : bool default/False →　昇順に圧縮　True→降順に圧縮
        """
        *tmp, = set(lst)
        tmp.sort(reverse=rev)
        self.__compress = {e: i for i, e in enumerate(tmp)}
        self.__uncompress = {i: e for i, e in enumerate(tmp)}
        self.__compress_len = len(self.__compress)

    def get_dict_lst_to_i(self):
        """
        O(1)
        :return: dict 圧縮データ
        """
        return self.__compress

    def get_dict_i_to_lst(self):
        """
        O(1)
        :return: dict 解凍データ
        """
        return self.__uncompress

    def get_data_lst_to_i(self, lst_data):
        """
        lst_dataが何番目の要素か返す(0スタート)
        :param lst_data: valiant 圧縮する前のデータ
        :return: int 圧縮後のデータ
        """
        return self.__compress[lst_data]

    def get_data_i_to_lst(self, i):
        """
        i番目の要素の圧縮前のデータを返す
        :param i: int 圧縮した後のデータ（順位）
        :return: 順位に対応した圧縮前のデータ
        """
        return self.__uncompress[i]

    def get_len(self):
        """
        :return: 圧縮後のデータ数
        """
        return self.__compress_len

N,M = IIS()
A,B,C,D,E,F = IIS()
XY = LLIIS(M)
XY.sort(key=lambda x:(x[0],x[1]))

XX = [x for x,_ in XY]
YY = [y for _,y in XY]

# XY = set()
# for _ in range(M):
#     x,y = IIS()
#     XY.add((x,y))


# 考えうる座標を全て取得
X = set()
for i in range(N+1):
    for j in range(N+1):
        if i+j > N:
            break
        for k in range(N+1):
            if i+j+k > N:
                continue
            X.add(A*i+C*j+E*k)

Y = set()
for i in range(N+1):
    for j in range(N+1):
        if i+j > N:
            break
        for k in range(N+1):
            if i+j+k > N:
                break
            Y.add(B*i+D*j+F*k)

X_C = COMPRESS(X)
Y_C = COMPRESS(Y)

dp = [[0] * (len(Y)+1) for _ in range(len(X)+1)]

H = len(X)
W = len(Y)

#初期位置
dp[X_C.get_data_lst_to_i(0)][Y_C.get_data_lst_to_i(0)] = 1

for _ in range(N):
    now = [[0] * (len(Y)+1) for _ in range(len(X)+1)]
    for h in range(H):
        for w in range(W):
            if not dp[h][w]:
                continue
            x = X_C.get_data_i_to_lst(h)
            y = Y_C.get_data_i_to_lst(w)

            for l,r in [[A,B],[C,D],[E,F]]:
                tl = bisect.bisect_left(XX,x+l)
                tr = bisect.bisect_right(XX,x+l)
                if tl < M and XX[tl] == x+l:
                    q = bisect.bisect_left(YY[tl:tr], y+r)
                    if q+tl<M and YY[tl+q] == y+r:
                        continue

                # if (x+l,y+r) in XY:
                #     continue
                tx = X_C.get_data_lst_to_i(x+l)
                ty = Y_C.get_data_lst_to_i(y+r)

                now[tx][ty] += dp[h][w] % 998244353
    dp = now

ans = 0
for d in dp:
    for a in d:
        ans += a
        ans %= 998244353
print(ans)




# N,M = IIS()
# A,B,C,D,E,F = IIS()
# XY = set()
# for _ in range(M):
#     x,y = IIS()
#     XY.add((x,y))
#
# dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
#
# for n in range(N):
#     now = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
#
#     for i in range(N+1):
#         for j in range(N+1):
#             if i+j > 300:
#                 break
#             for k in range(N+1):
#                 if i+j+k > 300:
#                     break
#
#                 x = i*A+j*C+k*E
#                 y = i*B+j*D+k*F
#
#                 if not (x+A,y+B) in XY:
#                     now[i+1][j][k] +=

