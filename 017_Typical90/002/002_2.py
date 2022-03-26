def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

# bit全探索
N = II()
ALL = 2 ** N
ans = []
for n in range(ALL):
    s = ''
    for i in range(N):
        if has_bit(n, i):
            s += '('
        else:
            s += ')'

    # カッコ列が正しいか判定
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        ans.append(s)

ans.sort()
for a in ans:
    print(a)