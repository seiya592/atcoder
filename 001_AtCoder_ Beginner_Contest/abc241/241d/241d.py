def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

Q = II()
query = [LIIS() for _ in range(Q)]
# A = [0] * ((10 ** 18) + 1)
A = []


def binary_search(lst, value, inf=False, mod=False):
    L_i = 0
    R_i = len(lst) - 1

    while L_i <= R_i:
        M_i = (L_i + R_i) // 2

        if value < lst[M_i]:
            R_i = M_i - 1
            continue
        if value > lst[M_i]:
            L_i = M_i + 1
            continue
        return M_i

    if mod:
        return L_i
    if inf:
        return R_i


flg = False
for q in query:
    if q[0] == 1:
        n, x = q
    else:
        n, x, k = q

    if n == 1:
        A.append(x)
        flg = True
        continue
    if flg:
        A.sort()
        flg = False
    if n == 2:
        tmp = binary_search(A, x, mod=True)
        if tmp - k >= 0:
            print(A[tmp - k])
        else:
            print(-1)
        continue
    if n == 3:
        tmp = binary_search(A, x, inf=True)
        if tmp + k < len(A):
            print(A[tmp + k])
        else:
            print(-1)
        continue



