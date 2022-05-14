def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


def func1():
    # for文とシグマ計算_1
    print(sum([i for i in range(1,II()+1)]))


def func2():
    # for文とシグマ計算_2
    L, R = IIS()
    print(sum([(2*i-1)**2 for i in range(L,R+1)]))


def func3():
    # for文とシグマ計算_3
    N,M = IIS()
    A = LIIS()
    B = LIIS()

    print(sum([(A[i]+B[j]) for i in range(N) for j in range(M)]))


def func4():
    # for文とシグマ計算_3
    N = II()
    print(sum([i*j for i in range(1,N) for j in range(i+1, N+1)]))


def func5():
    # for文とシグマ計算_4
    N = II()
    A = LIIS()
    ans = 1
    for i in range(N):
        ans = (ans * A[i]) % 10
    print(ans)

if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    func5()