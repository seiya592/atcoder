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
INF = 10**10
def RunLengthEncoding(iterator):
    """
    :param iterator:文字列やリストなど
    :return: [[文字列a,連続している数],[文字列b,連続している数]]
    """
    import itertools
    return [[key, len(list(group))]for key, group in itertools.groupby(iterator)]

S = I()

print(len(RunLengthEncoding(S))-1)