def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

S = I()
ALL = 2 ** (len(S)-1)
ans = 0
for n in range(ALL):
    lst = []
    num = S[0]
    for i in range(len(S)-1):
        if has_bit(n,i):
            lst.append(int(num))
            num = S[i+1]
        else:
            num += S[i+1]
    else:
        lst.append(int(num))
    ans += sum(lst)
print(ans)
