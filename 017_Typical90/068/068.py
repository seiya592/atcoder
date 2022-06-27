def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        """
        parent[i] : i番目の親 , 根の場合は負数(絶対値はその根の持つ要素数)
        :param n: 要素数
        """
        self.n = n                  # 要素数
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根の要素番号を返す
        :return:int xの根の要素番号
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループとを併合する
        """
        x = self.find(x)        # 要素xの根
        y = self.find(y)        # 要素yの根
        if x == y:
            return

        # Union by Size
        # サイズが大きいほうに小さいほうを加える
        if self.parents[x] > self.parents[y]:   # サイズが負数で格納されているため、この場合yのほうが大きい場合
            x, y = y, x     # xとy入れ替え

        # xが大きい状態
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズ（要素数）を返す
        """
        return -self.parents[self.find(x)]  # 負数で管理している為　-付ける

    def same(self, x, y):
        """
        要素x, yが同じグループに属するかどうかを返す
        :return:True→同じグループ
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        O(NlogN)
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        O(n)
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す　0が使われない頂点の場合0が孤立した根になっていることに注意！！！！
        O(n)
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        O(NlogN)
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print()での表示用
        ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        O(NlogN)
        """
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N = II()
Q = II()
TXYV = LLIIS(Q)

E = [-1]*(N+1)

for t,x,y,v in TXYV:
    if t == 1:
        continue
    E[y] = v

dist = [0] * (N+1)

for i in range(N+1):
    if E[i] == -1:
        continue
    dist[i] = E[i] - dist[i-1]

uf = UnionFind(N+1)

for t,x,y,v in TXYV:
    if not t:
        uf.union(x,y)
    else:
        if uf.same(x,y):
            if (x + y) % 2 == 0:
                print(dist[y] + (v - dist[x]))
            else:
                print(dist[y] - (v- dist[x]))
        else:
            print('Ambiguous')