def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


def func1():
    # 共通する数 (A ∩ B)
    N, M = IIS()
    A = set(LIIS())
    B = set(LIIS())
    ans = sorted(list(A & B))
    print(*ans)


def func2():
    # 数の合併 (A ∪ B)
    N, M = IIS()
    A = set(LIIS())
    B = set(LIIS())
    ans = sorted(list(A | B))
    for a in ans:
        print(a)


def func3():
    # 書かれた数の個数 (1)
    N, X = IIS()
    print(len([i for i in range(1, N + 1) if i % X == 0]))


def func4():
    # 書かれた数の個数(2)
    N,X,Y = IIS()
    A = set([i for i in range(1,N+1) if i % X == 0])
    B = set([i for i in range(1,N+1) if i % Y == 0])
    print(len(A & B))


def func5():
    # 含まれない数
    N, M = IIS()
    A = set(LIIS())
    B = set(LIIS())
    for a in sorted(list(A^B)):
        print(a)


def func6():
    # 合併後の個数
    N,M,K = IIS()
    print(N+M-K)


def func7():
    # 書かれた数の個数(3)
    N,X,Y = IIS()
    A = set(LIIS())
    B = set(LIIS())
    print((len(set(range(1,N+1)) ^ (A | B))))


def func8():
    # 書かれた数の個数(4)
    N = II()
    print(N - (N//3) - (N//5) + (N//15))

if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    # func5()
    # func6()
    # func7()
    func8()