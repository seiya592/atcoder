def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


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

N = II()
LOGIN = [LIIS() for _ in range(N)]

tmp = []
for a, b in LOGIN:
    tmp.append(a)
    tmp.append(a+b)

C = COMPRESS(tmp)

# いもす法
person = [0] * (C.get_len())

for a, b in LOGIN:
    person[C.get_data_lst_to_i(a)] += 1     # 圧縮した日付でカウント
    person[C.get_data_lst_to_i(a+b)] -= 1

ans = [0] * (N+1)
person_count = 0
for i in range(C.get_len()-1):
    person_count += person[i]
    ans[person_count] += C.get_data_i_to_lst(i+1) - C.get_data_i_to_lst(i)      # 圧縮した日付を解凍して差分計算

print(*ans[1:])

