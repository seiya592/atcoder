def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(input().split())

N = II()
S = [I() for _ in range(N)]


for i in range(N):
    for j in range(N):
        #横チェック
        if N - j >= 6:
            if S[i][j:j+6].count('#') >= 4:
                print('Yes')
                exit()
        #縦チェック
        if N - i >= 6:
            if (S[i][j] + S[i+1][j] + S[i+2][j] + S[i+3][j] + S[i+4][j] + S[i+5][j]).count('#') >= 4:
                print('Yes')
                exit()
        #右下方向
        if N - j >= 6 and N - i >= 6:
            if (S[i][j] + S[i+1][j+1] + S[i+2][j+2] + S[i+3][j+3] + S[i+4][j+4] + S[i+5][j+5]).count('#') >= 4:
                print('Yes')
                exit()
        #左上方向
        if i >= 5 and N - j >= 6:
            if (S[i][j] + S[i - 1][j + 1] + S[i -2][j + 2] + S[i - 3][j + 3] + S[i - 4][j + 4] + S[i- 5][j + 5]).count('#') >= 4:
                print('Yes')
                exit()

print('No')

