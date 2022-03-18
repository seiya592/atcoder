def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
QN = II()
Q = [LIIS() for _ in range(QN)]

row_list = list(range(N+1))
col_list = list(range(N+1))
rev = False

for q in Q:
    if q[0] == 1:
            row_list[q[1]], row_list[q[2]] = row_list[q[2]], row_list[q[1]]
    elif q[0] == 2:
            col_list[q[1]], col_list[q[2]] = col_list[q[2]], col_list[q[1]]
    elif q[0] == 3:
        row_list, col_list = col_list, row_list
        rev = not rev
    else:
        if rev:
            #反転
            ans = N * (col_list[q[2]] - 1) + row_list[q[1]] - 1
        else:
            ans = N * (row_list[q[1]] - 1) + col_list[q[2]] - 1
        print(ans)
