# 使用例
# https://atcoder.jp/contests/abc221/submissions/30500523
# https://atcoder.jp/contests/abc036/submissions/30497736

# 一次元リスト座標圧縮  https://tjkendev.github.io/procon-library/python/geometry/compress.html
def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)))}
# def COMPRESS(arr):    # この関数と同等
#     *XS, = set(arr)
#     XS.sort()
#     return {e: i for i, e in enumerate(XS)}

# 一次元リスト座標復元用
def UNCOMPRESS(arr): return {i: e for i, e in enumerate(sorted(set(arr)))}


# クラス化 自作

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