def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
import string
sys.setrecursionlimit(10000000)


class CALC_NEXT:
    """
    target_string の i文字目を基準に最初にcheck_lstの文字が出現するindex
    """
    def __init__(self, target_string, check_lst=[]):
        """
        O(|target_string| * |check_lst|)
        :param target_string:
        :param check_lst:
        """
        self.__S = target_string        # チェックする文字列
        self.__check_lst = check_lst if check_lst else string.ascii_lowercase

        N = len(self.__S)
        S = self.__S
        nex = [{} for _ in range(N)]
        # nex[i文字目]{key='a-z':value=i文字目から見て最短で何番目に存在するか}

        # init
        for s in string.ascii_lowercase:
            nex[N - 1][s] = -1
        nex[N - 1][S[N - 1]] = 0

        # 後ろから詰めていく
        for i in reversed(range(N - 1)):
            for a in string.ascii_lowercase:
                if S[i] == a:
                    nex[i][a] = 0
                else:
                    nex[i][a] = nex[i + 1][a] + 1 if nex[i + 1][a] != -1 else -1

        self.__calc_next = nex

    def get_calc_next_list(self):
        """
        O(1)
        :return:calc_next[i文字目]{key='a-z' or 指定したリストの要素 :value=i文字目から見て最短で何番目に存在するか}
        """
        return self.__calc_next


N, K = IIS()
S = I()
nex = CALC_NEXT(S).get_calc_next_list()

# 貪欲法
# 先頭になりえる文字列でaに近い文字を探していく
ans = ''
k = K
now = 0
while True:
    for a in string.ascii_lowercase:
        if nex[now][a] != -1 and N - (nex[now][a] + now) >= k:
            ans += a
            k -= 1
            now += nex[now][a] + 1
            break
    if k <= 0:
        break
print(ans)