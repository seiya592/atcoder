# https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html

#　強連結成分 (SCC)
# DFSをしているのでpython提出！！！！
class StronglyConnectedComponent:
    """
    強連結成分 (SCC)
    互いに行き来が可能な頂点の集合を求める
    有向グラフであること。
    """

    def __init__(self,n):
        """
        :param n: 頂点数
        """
        self.__num = n
        self.__edge = [set([]) for _ in range(n+1)]     # [0]は使用しない 通常の有向辺
        self.__r_edge = [set([]) for _ in range(n+1)]   # [0]は使用しない　反転させた有向辺
        self.__rank = []    # 頂点のランク dfsで一番奥から求める
        self.__group = []

    def add_edge(self,frm, to):
        """
        辺の追加
        :param frm: 出発点
        :param to:行き先
        """
        self.__edge[frm].add(to)
        self.__r_edge[to].add(frm)

    def solve(self):
        """
        :return:  強連結成分分解した頂点のリスト　DAG順に並んでいる
        """
        # ランク付け
        done = [False] * (self.__num + 1)
        self.__rank = []
        for i in range(1, self.__num + 1):
            if not done[i]:
                self.__dfs(i, done)

        # 強連結成分を求める
        done = [False] * (self.__num + 1)
        self.__group = []
        for r in reversed(self.__rank):
            if not done[r]:
                self.__group.append([])  # 次のグループのリスト
                self.__dfs2(r, done)      # 1つのグループは有向辺を逆にした時に繋がっている
        return self.__group



    def __dfs(self, n, done):
        """
        rank付
        :param n:頂点
        """
        done[n] = True
        for e in self.__edge[n]:
            if not done[e]:
                self.__dfs(e, done)
        self.__rank.append(n)

    def __dfs2(self, n, done):
        """
        SCCを求める
        """
        done[n] = True

        for e in self.__r_edge[n]:
            if not done[e]:
                self.__dfs2(e, done)
        self.__group[-1].append(n)