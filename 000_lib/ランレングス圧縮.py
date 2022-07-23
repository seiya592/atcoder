import itertools
def RunLengthEncoding(iterator):
    """
    :param iterator:文字列やリストなど
    :return: [[文字列a,連続している数],[文字列b,連続している数]・・・]
    """

    return [[key, len(list(group))]for key, group in itertools.groupby(iterator)]