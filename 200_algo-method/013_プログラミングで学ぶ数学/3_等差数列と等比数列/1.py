def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


def func1():
    # 500円玉貯金
    N,X = IIS()
    tmp = X
    for i in range(N+1):
        print(tmp)
        tmp += 500


def func2():
    # 貯金計画
    A,B,X,Y = IIS()
    t = (Y-X) // (B-A)
    print(X-(t*A))


def func3():
    # 等差数列の和_1
    N = II()
    print((N+1) * N // 2)


def func4():
    N,X,D = IIS()
    # N-1項を求める
    m = (N-1) * D + X

    print((X + m) * N // 2)


if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    func4()
    # func5()
    # func6()
    # func7()
    # func8()