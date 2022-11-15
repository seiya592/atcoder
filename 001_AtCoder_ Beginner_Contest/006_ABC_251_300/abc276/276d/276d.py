"""
2022/11/05 20:57:35
"""
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17

"""
1 ~ 2*10**5 までの値すべてに使用した場合、for文が59528480回  計算時間は833[ms]
"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def factorization_count(n):
    """
    O(N loglog N)   10**7は437ms  3*10**7で1293ms（現実的なのはここくらいまで？）
    2~nまでの素因数の 「種類」 をカウント
    :param n: 上限
    :return: list型 0~Nの素因数の種類数 (0,1は未定義（0）)
    """
    arr = [0] * (n + 1)
    for i in range(2, n + 1):
        if arr[i]:
            continue
        j = 1
        while i * j <= n:
            arr[i * j] += 1
            j += 1
    return arr

N = II()
A = LIIS()

ans = 0
check = -1
_2_cnt = INF
_3_cnt = INF
for a in A:
    D = factorization(a)
    tmp = 1
    flg_2 = False
    flg_3 = False
    for n,c in D:
        if n == 2 or n == 3:
            if n == 2:
                _2_cnt = min(_2_cnt, c)
                flg_2 = True

            else:
                _3_cnt = min(_3_cnt, c)
                flg_3 = True
            ans += c
        else:
            tmp *= n**c

    if not flg_2:
        _2_cnt = 0
    if not flg_3:
        _3_cnt = 0

    if check == tmp or check == -1:
        check = tmp
    else:
        print(-1)
        exit()
print(ans-(_2_cnt*N)-(_3_cnt*N))