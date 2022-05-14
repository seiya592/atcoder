def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()

S = LLIIS(N)
T = LLIIS(N)

def func(N,S):
    xs, xe, ys, ye = N, 0, N, 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                xs = min(xs,i)
                xe = max(xe,i)
                ys = min(ys,j)
                ye = max(ye,j)
    a,b,c,d =  xs, xe+1, ys, ye+1

    SS = [[''] * (d-c) for _ in range(b-a)]
    for i in range(b-a):
        for j in range(d-c):
            SS[i][j] = S[a+i][c+j]
    return SS

S = func(N,S)
T = func(N,T)



for i in range(4):
    if len(S) == len(T) and len(S[0]) == len(T[0]):
        flg = True
        for rs,rt in zip(S,T):
            for s, t in zip(rs,rt):
                if s!= t:
                    flg = False
        if flg:
            print('Yes')
            exit()
    #回転させる
    Tt = []
    for x in zip(*T[::-1]):
        Tt.append(x)
    T = Tt
print('No')
