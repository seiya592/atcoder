def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
# https://algo-method.com/courses/13

def func1():
    # ランチセット
    N,M = IIS()
    print(N*M)


def func2():
    # 2 つのサイコロ (1)
    N = II()
    ans = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j == N:
                ans += 1
    print(ans)


def func3():
    # 2 つのサイコロ (2)
    X,Y = IIS()
    ans = 0
    for i in range(1,7):
        for j in range(1,7):
            if i+j == X or i+j == Y:
                ans += 1
    print(ans)


def func4():
    # パスワードの可能性 (1)
    _, __ = IIS()
    A = LIIS()
    B = LIIS()
    ans = 0
    for i in range(10):
        for j in range(10):
            if i in A and j in B:
                ans += 1
    print(ans)


def func5():
    # ラッキーナンバー (1)
    N = II()
    _ = LIIS()
    print(N**3)

def func6():
    # ラッキーナンバー (2)
    N = II()
    _ = LIIS()
    print(10**3 - ((10-N) ** 3))


def func7():
    # ボールと箱 (1)
    N, M = IIS()
    ans = 1
    for i in range(N,(N-M),-1):
        ans *= i
    print(ans)


if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    # func5()
    # func6()
    func7()
    # func8()