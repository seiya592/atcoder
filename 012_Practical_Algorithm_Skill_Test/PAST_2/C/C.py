def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(str,input().split()))


N = II()
S = [input() for _ in range(N)]

iLen = N
jLen = 2 * N - 1

ans = [[''] * jLen for _ in range(N)]

for i in range(iLen):
    for j in range(jLen):
        ans[iLen - 1 - i][jLen - 1 - j] = S[iLen - 1 - i][jLen - 1 - j]

        if i != 0 and ans[iLen - 1 - i][jLen - 1 - j] == '#':
            if ans[iLen - 1 - i + 1][jLen - 1 - j] == 'X':
                ans[iLen - 1 - i][jLen - 1 - j] = 'X'
            if jLen - 1 - j - 1 >= 0:
                if ans[iLen - 1 - i + 1][jLen - 1 - j - 1] == 'X':
                    ans[iLen - 1 - i][jLen - 1 - j] = 'X'
            if j >= 0:
                if ans[iLen - 1 - i + 1][jLen - 1 - j + 1] == 'X':
                    ans[iLen - 1 - i][jLen - 1 - j] = 'X'

for a in ans:
    print(''.join(a))
