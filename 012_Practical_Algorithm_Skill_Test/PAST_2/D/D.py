#https://atcoder.jp/contests/past202004-open/tasks/past202004_d
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

def is_match(S,T):
    #Tは最大3文字
    Tlen = len(T)
    flg = False

    for i in range(len(S) - (Tlen -1)):
        # if S[i] == T[0] or S[i] == '.':
        for t in range(0, Tlen):
            if S[i + t] == T[t] or T[t] == '.':
                flg = True
            else:
                flg = False
                break
        if flg:
            break
    return flg


C = 'abcdefghijklmnopqrstuvwxyz.'
S = I()
ans = []
for T in C:
    if is_match(S,T):
        ans.append(T)

for T1 in C:
    for T2 in C:
        T = T1+T2
        if is_match(S,T):
            ans.append(T)

for T1 in C:
    for T2 in C:
        for T3 in C:
            T = T1 + T2 + T3
            if is_match(S,T):
                ans.append(T)

print(len(ans))