import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10
import bisect
def div_count(N):
    """
    1~Nまでの各値の約数の数をカウント
    O(NLogN)
    :return:List
    """
    div = [0] * (N+1)
    for n in range(1,N+1):
        for a in range(n, N+1, n):  #a = nからnステップ毎の値 →　div[a]約数にnが含まれている
            div[a] += 1
    return div

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = II()

lst = []
lst2 = []
done = {}
for i in range(N+1):
    ii = i*i
    lst.append(ii)
    lst2.append(i)
    done[ii] = False
data = {}
data[1] = [1]
for i, l in enumerate(lst[2:],start=2):
    if l not in data:
        data[l] = make_divisors(l)
        k = l
        while k <= N:
            j = k ** 2
            data[j] = data[k] + [j // data[k][len(data[k])-2]]
            for z in range(len(data[k])-3,-1,-1):
                data[j] = data[j] + [j // data[k][z]]
            k = j



ans = 0
# div_list = []
for l in lst[1:]:
    div = data[l]
    # div_list.append(div)
    i = bisect.bisect_right(div,N)
    ans += len(div)
    ans -= 0 if i == len(div) else (len(div) - i) * 2
print(ans)
# print(*div_list)